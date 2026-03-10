import os
from app import create_app

# Read config name from env, default to development
config_name = os.getenv("FLASK_ENV", "development")
app = create_app(config_name)

if __name__ == "__main__":
    # Only use the dev server locally
    # Port 5001
    app.run(host="0.0.0.0", port=5001, debug=(config_name == "development"))
