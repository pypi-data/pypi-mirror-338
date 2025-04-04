#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main entry point for running auto-python-toolkit as a module:
python -m auto_python_toolkit
"""

import sys
from .cli import main

if __name__ == "__main__":
    sys.exit(main()) 