@echo off
REM Windows setup script
REM Run once to create venv, install deps, and init DB
REM Usage: setup.bat

echo = Creating virtual environment =
python -m venv venv

echo = Activating virtual environment =
call venv\Scripts\activate.bat

echo = Installing dependencies =
pip install --upgrade pip
pip install -r requirements.txt

if not exist .env (
    echo = Creating .env from .env.example =
    copy .env.example .env
    echo    Edit .env with your database credentials before running.
)

echo = Initializing database migrations =
flask --app run:app db init 2>nul || echo - migrations\ already exists, skipping init
flask --app run:app db migrate -m "initial" 2>nul || echo - no new migrations detected
flask --app run:app db upgrade

echo.
echo Setup complete!
echo - To start the server:
echo    - venv\Scripts\activate.bat
echo    - python run.py
