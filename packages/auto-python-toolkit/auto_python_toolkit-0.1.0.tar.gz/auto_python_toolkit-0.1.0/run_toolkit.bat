@echo off
echo === Auto Python Toolkit ===
echo Creating an offline-ready Python environment for your project

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python first: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if uv is installed
uv --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: 'uv' is not installed or not in PATH.
    echo Please install uv first: https://github.com/astral-sh/uv
    pause
    exit /b 1
)

REM Run the toolkit with all arguments passed to this script
python main.py %*

pause 