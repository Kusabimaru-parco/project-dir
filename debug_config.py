# debug_config.py
import os
from dotenv import load_dotenv

load_dotenv()

print("Environment Variables Check:")
print(f"DB_USER: '{os.getenv('DB_USER')}'")
print(f"DB_PASSWORD: '{os.getenv('DB_PASSWORD')}'") 
print(f"DB_HOST: '{os.getenv('DB_HOST')}'")
print(f"DB_NAME: '{os.getenv('DB_NAME')}'")

# Check if .env file is being found
from pathlib import Path
env_path = Path('.') / '.env'
print(f"\n.env file exists: {env_path.exists()}")
print(f"Current directory: {os.getcwd()}")