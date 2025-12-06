@echo off
REM CineFinds Quick Setup Script for Windows
REM This script automates the setup process

echo ========================================
echo   CineFinds - Quick Setup
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.10+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Python found!
echo.

REM Create virtual environment
echo [2/5] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created!
) else (
    echo Virtual environment already exists!
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate
echo.

REM Install dependencies
echo [4/5] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
echo.

REM Create .env file if it doesn't exist
if not exist .env (
    echo [5/5] Creating .env file...
    copy .env.example .env
    echo.
    echo [INFO] Please edit .env file with your configuration
) else (
    echo [5/5] .env file already exists
)
echo.

REM Run migrations
echo Running database migrations...
python manage.py migrate
echo.

echo ========================================
echo   Setup Complete! 
echo ========================================
echo.
echo To start the server, run:
echo   python manage.py runserver
echo.
echo Then open your browser to:
echo   http://127.0.0.1:8000/
echo.
pause
