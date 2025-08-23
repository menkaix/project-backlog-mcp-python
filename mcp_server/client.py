import os
from dotenv import load_dotenv
from mcp_server.generated_client.hypermanager_ia_gemini_integration_client import Client

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer les informations d'identification de l'environnement
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

# Initialiser le client API
client = Client(base_url=base_url, headers={"x-api-key": api_key})