@echo off

echo Creating virtual environment...
python -m venv .venv

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo Installing PyTorch with GPU support...
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121

echo Creating 'input' folder...
if not exist "input" mkdir input

echo Installation completed.
pause
