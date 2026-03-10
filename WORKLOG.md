# Work Log

## Jenna's work on 03/09

This session I set up the backend skeleton for our game portal. Here's a rundown:

### Project Setup
- Created the backend folder structure
- Added a `.gitignore` so we don't accidentally commit virtual environments, `.env` files, or other junk
- Set up a `requirements.txt` with all the Python packages we need (Flask, SQLAlchemy, Flask-CORS, Flask-Migrate, PyMySQL, etc.) We might need other things but not sure yet

### Flask 
- Built out the Flask app intializer/"factory" in `app/__init__.py`
- Added a config file (`app/config.py`)

### Database
- Created the `Game` model with all the fields we might need, but we should review this and you guys tell me if you agree with it
- Ran the initial database migration so the games table is ready to go

### APIs
For now I just put these in but didn't write any code for them yet
- **GET /api/games** 
- **GET /api/games/<id>**
- **POST /api/admin/games**
- **PUT /api/admin/games/<id>**
- **DELETE /api/admin/games/<id>**

### Crossplatform to run on windows and macOS (and Linux in case someone at Hewitt uses that)
- Added `setup.sh` and `setup.bat` scripts so both Mac/Linux and Windows users can set up the project with one command
- Added `start.sh` and `start.bat` to start the dev server easily on either platform

### Run It
Right now we can't use these commands to run it yet because our database connection isn't actually configured yet, but once we get that figured it out we'll be able to run it like this: 
From the `backend/` folder:
- **Mac/Linux:** `bash setup.sh` then `bash start.sh`
- **Windows:** `setup.bat` then `start.bat`

The server runs on port 5001

### TODO tasks
You can also checkout my "TODO" comments that I left in some of the files
- Create database server on MariaDB and set up our configuration so we can all get connected with it
- Fully set up all of the APIs that we need and fill them in with code.
- Think whether we need any more database models and write those out
- Figure out where we're going to get our games from when we talk to Hewitt

Later on, we can add:
- JWT auth and admin only checks for authorizing requests to admin endpoints
- Maybe set up some workflows? 
- Once all the APIs are decided on, we don't necessarily need them to work, but then we can start working on the frontend

