#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
from .toolkit import AutoPythonToolkit
from . import __version__


def main():
    """
    Command line entry point for auto-python-toolkit.
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Auto Python Toolkit - Create offline Python environments"
    )
    parser.add_argument(
        '--version', 
        action='version', 
        version=f'auto-python-toolkit v{__version__}'
    )
    parser.add_argument(
        '--auto', 
        action='store_true', 
        help='Automatically use default Python version without prompting'
    )
    parser.add_argument(
        '--lang', 
        choices=['en', 'zh_CN'], 
        help='Set interface language (en/zh_CN)'
    )
    args = parser.parse_args()
    
    # Run the toolkit
    toolkit = AutoPythonToolkit(lang=args.lang)
    toolkit.run(use_default_python=args.auto)
    
    return 0


if __name__ == "__main__":
    sys.exit(main()) 