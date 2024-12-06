import httpx
from app.config import TOKEN_URL, CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPES

async def exchange_code_for_token(code: str):
    """
    Exchanges the authorization code for an access token.
    """
    token_data = {
        "client_id": CLIENT_ID,
        "scope": SCOPES,
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
        "client_secret": CLIENT_SECRET,
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    async with httpx.AsyncClient() as client:
        response = await client.post(TOKEN_URL, data=token_data, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error exchanging code: {response.text}")

    return response.json()
