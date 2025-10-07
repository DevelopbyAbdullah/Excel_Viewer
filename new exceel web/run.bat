@echo off
echo Installing required packages...
pip install -r requirements.txt

echo Starting the web application...
python app.py

pause