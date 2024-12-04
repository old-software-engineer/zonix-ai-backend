from pydantic import BaseModel

class AuthToken(BaseModel):
    email: str
    name: str
    microsoft_id: str
