#!/usr/bin/env bash
# macOS / Linux setup script
# Run once to create venv, install deps, and init DB
# Usage: bash setup.sh
set -e

echo "= Creating virtual environment ="
python3 -m venv venv

echo "= Activating virtual environment ="
source venv/bin/activate

echo "= Installing dependencies ="
pip install --upgrade pip
pip install -r requirements.txt


if [ ! -f .env ]; then
    echo "= Creating .env from .env.example ="
    cp .env.example .env
    echo "(Edit .env with your database credentials before running)"
fi

echo "= Initializing database migrations ="
flask --app run:app db init 2>/dev/null || echo " - (migrations/ already exists, skipping init)"
flask --app run:app db migrate -m "initial" 2>/dev/null || echo " - (no new migrations detected)"
flask --app run:app db upgrade

echo ""
echo "Setup complete"
echo " - To start the server:"
echo "      - source venv/bin/activate"
echo "      - python run.py"
