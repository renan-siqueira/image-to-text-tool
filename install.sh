#!/bin/bash

# Creating virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv

# Activating virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Installing dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Installing custom version of PyTorch
echo "Installing PyTorch with GPU support..."
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121

# Creating 'input' folder
echo "Creating 'input' folder..."
mkdir -p input

# Creating 'json' folder
echo "Creating 'json' folder..."
mkdir -p json

echo "Installation completed."
