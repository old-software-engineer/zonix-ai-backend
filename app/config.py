import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:8000/auth/callback", )
TENANT_ID = os.getenv("TENANT_ID")

AUTH_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize"
TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
GRAPH_URL = "https://graph.microsoft.com/v1.0"
SCOPES = "User.Read TeamMember.Read.All Team.ReadBasic.All GroupMember.ReadWrite.all Group.Read.All Group.ReadWrite.All"