import httpx
from app.config import GRAPH_URL

async def fetch_user_profile(access_token: str):
    """
    Fetches the user's profile from Microsoft Graph.
    """
    url = f"{GRAPH_URL}/me"
    headers = {"Authorization": f"Bearer {access_token}"}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error fetching profile: {response.text}")

    return response.json()
