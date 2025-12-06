#!/bin/bash
# CineFinds Quick Setup Script for macOS/Linux
# This script automates the setup process

echo "========================================"
echo "  CineFinds - Quick Setup"
echo "========================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.10+ from https://www.python.org/"
    exit 1
fi

echo "[1/5] Python found!"
echo ""

# Create virtual environment
echo "[2/5] Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created!"
else
    echo "Virtual environment already exists!"
fi
echo ""

# Activate virtual environment
echo "[3/5] Activating virtual environment..."
source venv/bin/activate
echo ""

# Install dependencies
echo "[4/5] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
echo ""

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "[5/5] Creating .env file..."
    cp .env.example .env
    echo ""
    echo "[INFO] Please edit .env file with your configuration"
else
    echo "[5/5] .env file already exists"
fi
echo ""

# Run migrations
echo "Running database migrations..."
python manage.py migrate
echo ""

echo "========================================"
echo "  Setup Complete!"
echo "========================================"
echo ""
echo "To start the server, run:"
echo "  python manage.py runserver"
echo ""
echo "Then open your browser to:"
echo "  http://127.0.0.1:8000/"
echo ""
