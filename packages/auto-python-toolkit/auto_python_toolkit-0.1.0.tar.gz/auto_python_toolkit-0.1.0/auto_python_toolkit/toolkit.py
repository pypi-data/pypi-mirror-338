#!/usr/bin/env python
# -*- coding: utf-8 -*-

# /// script
# dependencies = [
#   "requests<3",
#   "rich",
#   "pandas",
#   "tqdm",
#   "termcolor",
#   "progressbar",
#   "xlrd",
#   "openpyxl",
# ]
# ///

import os
import sys
import platform
import subprocess
import shutil
import argparse
from pathlib import Path
import json
import re
import locale
from typing import Dict, List, Tuple, Optional

from .dependency_analyzer import DependencyAnalyzer
from .i18n import get_translator


class AutoPythonToolkit:
    """
    A tool to create an offline-ready Python environment for a project.
    Uses uv to download Python, analyze dependencies, and package everything together.
    """
    
    def __init__(self, lang: str = None):
        self.project_dir = Path.cwd()
        self.output_dir = self.project_dir / "output"
        self.translator = get_translator(lang)
        self._ = self.translator.get  # 简化访问翻译的方法
        
        # 支持的Windows版本及其Python版本限制
        self.windows_versions = {
            "Windows 7 (64-bit)": {
                "min_py": "3.7", 
                "max_py": "3.7.9",
                "versions": ["3.7.9"]
            },
            "Windows 10 (32-bit)": {
                "min_py": "3.7", 
                "max_py": "3.11.11",
                "versions": ["3.7.9", "3.8.20", "3.9.21", "3.10.16", "3.11.11"]
            },
            "Windows 10 (64-bit)": {
                "min_py": "3.7", 
                "max_py": "3.13.2",
                "versions": ["3.7.9", "3.8.20", "3.9.21", "3.10.16", "3.11.11", "3.12.9", "3.13.2"]
            },
            "Windows 11 (64-bit)": {
                "min_py": "3.7", 
                "max_py": "3.14.0a6",
                "versions": ["3.7.9", "3.8.20", "3.9.21", "3.10.16", "3.11.11", "3.12.9", "3.13.2", "3.14.0a6"]
            },
            "Windows Server 2016 (64-bit)": {
                "min_py": "3.7", 
                "max_py": "3.11.11",
                "versions": ["3.7.9", "3.8.20", "3.9.21", "3.10.16", "3.11.11"]
            },
            "Windows Server 2019 (64-bit)": {
                "min_py": "3.7", 
                "max_py": "3.13.2",
                "versions": ["3.7.9", "3.8.20", "3.9.21", "3.10.16", "3.11.11", "3.12.9", "3.13.2"]
            },
            "Windows Server 2022 (64-bit)": {
                "min_py": "3.7", 
                "max_py": "3.14.0a6",
                "versions": ["3.7.9", "3.8.20", "3.9.21", "3.10.16", "3.11.11", "3.12.9", "3.13.2", "3.14.0a6"]
            }
        }
        
    def check_uv_installed(self) -> bool:
        """Check if uv is installed and available."""
        try:
            subprocess.run(["uv", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except (subprocess.SubprocessError, FileNotFoundError):
            return False
    
    def display_os_menu(self) -> str:
        """Display a menu for OS selection and return the selected OS."""
        print(f"\n{self._('os_menu_title')}")
        options = list(self.windows_versions.keys())
        
        for i, os_option in enumerate(options, 1):
            print(f"{i}. {os_option}")
        
        while True:
            try:
                choice = int(input(f"\n{self._('enter_choice')}"))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                print(self._("invalid_choice"))
            except ValueError:
                print(self._("invalid_choice"))
    
    def display_python_menu(self, target_os: str, use_default: bool = False) -> str:
        """
        Display a menu for Python version selection and return the selected version.
        
        Args:
            target_os: The target operating system
            use_default: If True, automatically return the default (max) version
            
        Returns:
            Selected Python version
        """
        if use_default:
            return self.windows_versions[target_os]["max_py"]
            
        print(f"\n{self._('python_menu_title')}")
        print(f"{self._('python_version_note')}")
        versions = self.windows_versions[target_os]["versions"]
        
        for i, version in enumerate(versions, 1):
            label = version
            if version == self.windows_versions[target_os]["max_py"]:
                label = f"{version} {self._('python_default_hint')}"
            print(f"{i}. {label}")
        
        while True:
            try:
                choice = int(input(f"\n{self._('enter_choice')}"))
                if 1 <= choice <= len(versions):
                    return versions[choice - 1]
                print(self._("invalid_choice"))
            except ValueError:
                print(self._("invalid_choice"))
    
    def find_python_files(self) -> List[Path]:
        """Find all Python files in the project directory."""
        return list(self.project_dir.glob("**/*.py"))
    
    def analyze_dependencies(self) -> List[str]:
        """
        Analyze Python files to detect import statements and identify dependencies
        using the advanced DependencyAnalyzer.
        """
        analyzer = DependencyAnalyzer()
        return analyzer.analyze_project(self.project_dir)
    
    def setup_virtual_env(self, target_os: str, py_version: str, dependencies: List[str]) -> bool:
        """
        Set up a virtual environment with uv for the specified OS
        and install the required dependencies.
        
        Args:
            target_os: The target operating system
            py_version: The Python version to use
            dependencies: List of dependencies to install
            
        Returns:
            True if successful, False otherwise
        """
        venv_path = self.project_dir / "venv"
        
        print(self._("setup_venv", py_version))
        
        # Get script dependencies if available
        script_deps = []
        main_py = self.project_dir / "main.py"
        
        if main_py.exists():
            analyzer = DependencyAnalyzer()
            script_deps = analyzer.extract_script_dependencies(main_py)
            
        # Use script dependencies if available, otherwise use detected dependencies
        final_dependencies = script_deps if script_deps else dependencies
        
        # Create virtual environment using uv
        try:
            subprocess.run(
                ["uv", "venv", str(venv_path), f"--python={py_version}"],
                check=True
            )
            
            # Install dependencies
            if final_dependencies:
                print(self._("installing_deps", ", ".join(final_dependencies)))
                subprocess.run(
                    ["uv", "pip", "install"] + final_dependencies,
                    check=True
                )
            
            # Generate requirements.txt file for reproducibility
            if final_dependencies:
                with open(self.project_dir / "requirements.txt", "w") as f:
                    for dep in final_dependencies:
                        f.write(f"{dep}\n")
            
            return True
        except subprocess.SubprocessError as e:
            print(self._("setup_error", str(e)))
            return False
    
    def package_project(self, target_os: str, py_version: str) -> bool:
        """
        Package the project with its virtual environment for offline use.
        
        Args:
            target_os: The target operating system
            py_version: The Python version used
            
        Returns:
            True if successful, False otherwise
        """
        output_name = f"auto-python-{target_os.replace(' ', '-').replace('/', '-')}-py{py_version}"
        output_path = self.output_dir / output_name
        
        print(self._("packaging_project", target_os))
        
        try:
            # Create output directory
            if output_path.exists():
                shutil.rmtree(output_path)
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Copy project files
            for item in self.project_dir.iterdir():
                if item.name not in [".git", "output", "venv"]:
                    if item.is_dir():
                        shutil.copytree(item, output_path / item.name)
                    else:
                        shutil.copy2(item, output_path)
            
            # Copy virtual environment
            shutil.copytree(self.project_dir / "venv", output_path / "venv")
            
            # Create a simple launcher script
            with open(output_path / "run_project.bat", "w") as f:
                f.write("@echo off\n")
                f.write("call venv\\Scripts\\activate.bat\n")
                f.write("echo Python environment is ready!\n")
                f.write("echo You can now run your Python scripts.\n")
                f.write("cmd /k\n")
            
            # Create a readme for the packaged project
            with open(output_path / "OFFLINE_README.md", "w") as f:
                f.write(f"# Offline Python Environment for {target_os} (Python {py_version})\n\n")
                f.write("This package contains a ready-to-use Python environment ")
                f.write("with all required dependencies for offline development.\n\n")
                f.write("## How to use\n\n")
                f.write("1. Extract this package to your desired location\n")
                f.write("2. Run the `run_project.bat` file to activate the Python environment\n")
                f.write("3. You can now run your Python scripts in the activated environment\n")
            
            # Create zip archive
            shutil.make_archive(str(output_path), 'zip', self.output_dir, output_name)
            print(self._("packaging_success", f"{output_path}.zip"))
            
            return True
        except Exception as e:
            print(self._("packaging_error", str(e)))
            return False
    
    def run(self, use_default_python: bool = False):
        """
        Run the main workflow.
        
        Args:
            use_default_python: If True, skip Python version selection and use default
        """
        print(self._("app_title"))
        print(self._("app_subtitle"))
        
        # Check if uv is installed
        if not self.check_uv_installed():
            print(self._("uv_not_installed"))
            print(self._("uv_install_hint"))
            return
        
        # Select target OS
        target_os = self.display_os_menu()
        print(self._("selected_os", target_os))
        
        # Select Python version
        python_version = self.display_python_menu(target_os, use_default_python)
        if use_default_python:
            print(self._("using_default_python", target_os))
        else:
            print(self._("selected_python", python_version))
        
        # Find Python files and analyze dependencies
        python_files = self.find_python_files()
        print(self._("found_files", len(python_files)))
        
        dependencies = self.analyze_dependencies()
        deps_str = ", ".join(dependencies) if dependencies else self._("no_deps")
        print(self._("detected_deps", deps_str))
        
        # Set up virtual environment
        if not self.setup_virtual_env(target_os, python_version, dependencies):
            print(self._("failed_setup"))
            return
        
        # Package project
        if not self.package_project(target_os, python_version):
            print(self._("failed_packaging"))
            return
        
        print(self._("done"))
        print(self._("output_location", self.output_dir)) 