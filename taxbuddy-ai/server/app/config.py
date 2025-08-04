import os
from dotenv import load_dotenv

# Load from the parent directory of this file (which is server/)
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

AZURE_SQL_URL = os.getenv("AZURE_SQL_CONNECTION_STRING")
