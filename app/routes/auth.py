from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import RedirectResponse
from app.config import AUTH_URL, REDIRECT_URI, CLIENT_ID, CLIENT_SECRET, TOKEN_URL
from app.services.microsoft_auth import exchange_code_for_token
import httpx


router = APIRouter()

@router.get("/login")
async def login():
    """
    Redirects the user to Microsoft's login page to authorize the app (multi-tenant).
    """
    auth_params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": REDIRECT_URI,
        "response_mode": "query",
        "scope": "User.Read offline_access openid profile",
    }
    auth_url = f"{AUTH_URL}?{'&'.join([f'{k}={v}' for k, v in auth_params.items()])}"
    return RedirectResponse(url=auth_url)


@router.get("/callback")
async def callback(request: Request):
    code = request.query_params.get("code")

    if not code:
        raise HTTPException(status_code=400, detail="Authorization code not provided")

    # Token exchange payload
    token_data = {
        "client_id": CLIENT_ID,
        "scope": "User.Read offline_access openid profile",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
        "client_secret": CLIENT_SECRET,
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    # Make the token request
    async with httpx.AsyncClient() as client:
        response = await client.post(TOKEN_URL, data=token_data, headers=headers)

    # Debugging logs
    print("Response Status:", response.status_code)
    print("Response Text:", response.text)

    # Handle response
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=f"Error exchanging code: {response.text}",
        )

    token_json = response.json()

    # Return the access and refresh tokens
    return {
        "access_token": token_json.get("access_token"),
        "refresh_token": token_json.get("refresh_token"),
        "expires_in": token_json.get("expires_in"),
        "id_token": token_json.get("id_token"),
    }