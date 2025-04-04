#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ast
import os
import sys
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple


class ImportVisitor(ast.NodeVisitor):
    """AST visitor to extract imports from Python code."""
    
    def __init__(self):
        self.imports = set()
        
    def visit_Import(self, node):
        for name in node.names:
            self.imports.add(name.name.split('.')[0])
        self.generic_visit(node)
        
    def visit_ImportFrom(self, node):
        if node.module is not None:
            self.imports.add(node.module.split('.')[0])
        self.generic_visit(node)


class DependencyAnalyzer:
    """
    Advanced dependency analyzer for Python projects.
    Scans Python files to detect imports and maps them to PyPI packages.
    """
    
    def __init__(self):
        self.standard_libs = self._get_standard_libraries()
        self.import_to_package_map = {
            # Common mappings of import names to package names
            'numpy': 'numpy',
            'pandas': 'pandas',
            'requests': 'requests',
            'flask': 'Flask',
            'django': 'Django',
            'pytest': 'pytest',
            'tensorflow': 'tensorflow',
            'torch': 'torch',
            'bs4': 'beautifulsoup4',
            'matplotlib': 'matplotlib',
            'sqlalchemy': 'SQLAlchemy',
            'cv2': 'opencv-python',
            'pil': 'pillow',
            'PIL': 'pillow',
            'sklearn': 'scikit-learn',
            'yaml': 'pyyaml',
            'dotenv': 'python-dotenv',
            'boto3': 'boto3',
            'psycopg2': 'psycopg2-binary',
            'pymongo': 'pymongo',
            'redis': 'redis',
            'fastapi': 'fastapi',
            'aiohttp': 'aiohttp',
            'selenium': 'selenium',
            'plotly': 'plotly',
            'dash': 'dash',
            'seaborn': 'seaborn',
            'jwt': 'pyjwt',
            # Add more mappings as needed
        }
    
    def _get_standard_libraries(self) -> Set[str]:
        """Get a list of standard library modules."""
        standard_libs = set(sys.builtin_module_names)
        
        # Add common standard library modules
        std_lib_modules = {
            'abc', 'argparse', 'array', 'ast', 'asyncio', 'base64', 'bisect', 
            'calendar', 'collections', 'concurrent', 'contextlib', 'copy', 
            'csv', 'ctypes', 'datetime', 'decimal', 'difflib', 'enum', 
            'filecmp', 'fnmatch', 'fractions', 'functools', 'glob', 'gzip', 
            'hashlib', 'heapq', 'hmac', 'html', 'http', 'importlib', 'inspect',
            'io', 'ipaddress', 'itertools', 'json', 'logging', 'math', 
            'mimetypes', 'multiprocessing', 'netrc', 'operator', 'os', 
            'pathlib', 'pickle', 'platform', 'pprint', 'queue', 
            'random', 're', 'shutil', 'signal', 'socket', 'sqlite3', 
            'statistics', 'string', 'struct', 'subprocess', 'sys', 'tempfile', 
            'textwrap', 'threading', 'time', 'timeit', 'traceback', 'types', 
            'typing', 'unicodedata', 'unittest', 'urllib', 'uuid', 'warnings',
            'weakref', 'xml', 'zipfile', 'zlib', 'configparser'
        }
        
        standard_libs.update(std_lib_modules)
        return standard_libs
    
    def parse_requirements_file(self, file_path: Path) -> List[str]:
        """Parse a requirements.txt file to extract package names."""
        if not file_path.exists():
            return []
        
        requirements = []
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                # Handle line continuation
                if line.endswith('\\'):
                    line = line[:-1].strip()
                
                # Handle version specifiers, extras and environment markers
                if '#' in line:
                    line = line.split('#')[0].strip()
                
                # Strip version specifiers
                package = re.split(r'[<>=!~;@]', line)[0].strip()
                
                # Strip extras
                if '[' in package:
                    package = package.split('[')[0].strip()
                
                if package:
                    requirements.append(package)
        
        return requirements
    
    def extract_script_dependencies(self, file_path: Path) -> List[str]:
        """
        Extract dependencies declared in the script using the format:
        # /// script
        # dependencies = [...]
        # ///
        """
        if not file_path.exists():
            return []
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Look for the script dependency pattern
        pattern = r"# /// script\s*\n(.*?)# ///"
        match = re.search(pattern, content, re.DOTALL)
        if not match:
            return []
        
        # Extract the dependencies list
        dep_section = match.group(1)
        dep_pattern = r"# dependencies\s*=\s*\[(.*?)\]"
        dep_match = re.search(dep_pattern, dep_section, re.DOTALL)
        if not dep_match:
            return []
        
        # Parse the dependencies
        deps_str = dep_match.group(1)
        deps = []
        for line in deps_str.split('\n'):
            # Extract package name from each line
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            # Remove quotes and commas
            line = line.strip('"\'').strip(',').strip()
            if line:
                # Strip version specifiers
                package = re.split(r'[<>=!~;@]', line)[0].strip()
                deps.append(package)
        
        return deps
    
    def get_imports_from_file(self, file_path: Path) -> Set[str]:
        """Extract all imports from a Python file using AST."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                tree = ast.parse(f.read())
                visitor = ImportVisitor()
                visitor.visit(tree)
                return visitor.imports
        except (SyntaxError, UnicodeDecodeError):
            # Fallback to regex-based extraction for files with syntax errors
            return self._extract_imports_with_regex(file_path)
    
    def _extract_imports_with_regex(self, file_path: Path) -> Set[str]:
        """Extract imports using regex as a fallback."""
        imports = set()
        import_patterns = [
            r'^\s*import\s+([a-zA-Z0-9_.]+)',
            r'^\s*from\s+([a-zA-Z0-9_.]+)\s+import'
        ]
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
            for pattern in import_patterns:
                for match in re.finditer(pattern, content, re.MULTILINE):
                    module = match.group(1).split('.')[0]
                    imports.add(module)
        
        return imports
    
    def analyze_project(self, project_path: Path) -> List[str]:
        """
        Analyze a Python project directory and return a list of 
        required PyPI packages.
        """
        python_files = list(project_path.glob('**/*.py'))
        
        # Check for script dependencies in main files
        script_deps = []
        main_files = [
            project_path / 'main.py',
            project_path / '__main__.py',
            project_path / 'app.py'
        ]
        
        for main_file in main_files:
            if main_file.exists():
                script_deps.extend(self.extract_script_dependencies(main_file))
        
        if script_deps:
            return sorted(list(set(script_deps)))
        
        # Check for existing requirements files
        req_files = [
            project_path / 'requirements.txt',
            project_path / 'pyproject.toml',
            project_path / 'setup.py'
        ]
        
        explicit_requirements = []
        for req_file in req_files:
            if req_file.exists() and req_file.name == 'requirements.txt':
                explicit_requirements.extend(self.parse_requirements_file(req_file))
        
        # If we found explicit requirements, use those
        if explicit_requirements:
            return explicit_requirements
        
        # Otherwise, analyze imports
        all_imports = set()
        for py_file in python_files:
            all_imports.update(self.get_imports_from_file(py_file))
        
        # Filter out standard library imports
        external_imports = all_imports - self.standard_libs
        
        # Map imports to package names
        packages = []
        for import_name in external_imports:
            package_name = self.import_to_package_map.get(import_name, import_name)
            packages.append(package_name)
        
        return sorted(list(set(packages)))


if __name__ == "__main__":
    # Simple test
    analyzer = DependencyAnalyzer()
    project_path = Path('.')
    dependencies = analyzer.analyze_project(project_path)
    print(f"Detected dependencies: {', '.join(dependencies)}") 