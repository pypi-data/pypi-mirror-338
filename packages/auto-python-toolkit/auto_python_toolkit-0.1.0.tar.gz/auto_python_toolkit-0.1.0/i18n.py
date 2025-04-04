#!/usr/bin/env python
# -*- coding: utf-8 -*-

import locale
import os
from typing import Dict, Any

# 支持的语言
SUPPORTED_LANGUAGES = ["en", "zh_CN"]

# 英文翻译
EN_TRANSLATIONS = {
    "app_title": "=== Auto Python Toolkit ===",
    "app_subtitle": "Creating an offline-ready Python environment for your project",
    "uv_not_installed": "Error: 'uv' is not installed or not in PATH.",
    "uv_install_hint": "Please install uv first: https://github.com/astral-sh/uv",
    "os_menu_title": "=== Select Target Operating System ===",
    "python_menu_title": "=== Select Python Version ===",
    "python_default_hint": "(default version for selected OS)",
    "python_version_note": "Note: uv supports Python 3.7+ only",
    "enter_choice": "Enter your choice (number): ",
    "invalid_choice": "Invalid choice. Please try again.",
    "selected_os": "Selected OS: {}",
    "selected_python": "Selected Python version: {}",
    "using_default_python": "Using default Python version for {}",
    "found_files": "Found {} Python files in the project",
    "detected_deps": "Detected dependencies: {}",
    "no_deps": "None",
    "setup_venv": "Setting up virtual environment with Python {}...",
    "installing_deps": "Installing dependencies: {}",
    "packaging_project": "Packaging project for {}...",
    "packaging_success": "Project packaged successfully: {}",
    "packaging_error": "Error packaging project: {}",
    "setup_error": "Error setting up virtual environment: {}",
    "failed_setup": "Failed to set up virtual environment.",
    "failed_packaging": "Failed to package project.",
    "done": "Done! Your project is now ready for offline use.",
    "output_location": "You can find the packaged project at: {}"
}

# 中文翻译
ZH_CN_TRANSLATIONS = {
    "app_title": "=== Python自动环境工具 ===",
    "app_subtitle": "为您的项目创建一个离线可用的Python环境",
    "uv_not_installed": "错误：'uv'未安装或不在PATH中。",
    "uv_install_hint": "请先安装uv：https://github.com/astral-sh/uv",
    "os_menu_title": "=== 选择目标操作系统 ===",
    "python_menu_title": "=== 选择Python版本 ===",
    "python_default_hint": "（所选操作系统的默认版本）",
    "python_version_note": "注意：uv仅支持Python 3.7及以上版本",
    "enter_choice": "请输入您的选择（数字）：",
    "invalid_choice": "无效的选择。请重试。",
    "selected_os": "已选择操作系统：{}",
    "selected_python": "已选择Python版本：{}",
    "using_default_python": "使用{}的默认Python版本",
    "found_files": "在项目中找到{}个Python文件",
    "detected_deps": "检测到的依赖项：{}",
    "no_deps": "无",
    "setup_venv": "正在使用Python {}设置虚拟环境...",
    "installing_deps": "安装依赖项：{}",
    "packaging_project": "正在为{}打包项目...",
    "packaging_success": "项目打包成功：{}",
    "packaging_error": "打包项目时出错：{}",
    "setup_error": "设置虚拟环境时出错：{}",
    "failed_setup": "无法设置虚拟环境。",
    "failed_packaging": "无法打包项目。",
    "done": "完成！您的项目现已准备好离线使用。",
    "output_location": "您可以在以下位置找到打包的项目：{}"
}

# 翻译映射
TRANSLATIONS = {
    "en": EN_TRANSLATIONS,
    "zh_CN": ZH_CN_TRANSLATIONS
}


class I18n:
    """国际化支持类"""
    
    def __init__(self, lang: str = None):
        """
        初始化I18n实例
        
        Args:
            lang: 手动指定语言代码，如不指定则自动检测系统语言
        """
        self.lang = lang or self._detect_system_language()
        self.translations = TRANSLATIONS.get(self.lang, EN_TRANSLATIONS)
    
    def _detect_system_language(self) -> str:
        """检测系统语言"""
        try:
            # 尝试获取系统语言设置
            system_lang, _ = locale.getdefaultlocale()
            
            # 如果是中文，返回zh_CN
            if system_lang and system_lang.startswith("zh"):
                return "zh_CN"
            
            # 否则返回英文
            return "en"
        except Exception:
            # 出错时默认使用英文
            return "en"
    
    def get(self, key: str, *args, **kwargs) -> str:
        """
        获取翻译文本
        
        Args:
            key: 翻译键
            *args, **kwargs: 用于format的参数
        
        Returns:
            翻译后的文本
        """
        text = self.translations.get(key, EN_TRANSLATIONS.get(key, key))
        
        if args or kwargs:
            try:
                return text.format(*args, **kwargs)
            except Exception:
                return text
        
        return text


def get_translator(lang: str = None) -> I18n:
    """
    获取翻译器实例
    
    Args:
        lang: 可选的语言代码
    
    Returns:
        I18n实例
    """
    return I18n(lang) 