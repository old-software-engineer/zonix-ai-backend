import os
from aiohttp import ClientSession

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")
REDIRECT_URI = os.getenv("REDIRECT_URI")
TOKEN_URL = f"https://login.microsoftonline.com/common/oauth2/v2.0/token"
AUTH_URL = f"https://login.microsoftonline.com/common/oauth2/v2.0/token"
SCOPES = "User.Read TeamMember.Read.All Team.ReadBasic.All"

def get_login_url():
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "response_mode": "query",
        "scope": SCOPES,
    }
    return f"{AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"

async def exchange_code_for_token(code: str):
    async with ClientSession() as session:
        data = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
        }
        async with session.post(TOKEN_URL, data=data) as response:
            return await response.json()
