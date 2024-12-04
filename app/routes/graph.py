from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.graph_api import fetch_user_profile
from app.models.user import User
from app.common.database import get_db

router = APIRouter()

@router.get("/me")
async def get_profile(access_token: str, db: Session = Depends(get_db)):
    try:
        # Fetch the user profile from Microsoft Graph
        profile = await fetch_user_profile(access_token)
        print("profile",profile)
        # Check if the user already exists in the database
        existing_user = db.query(User).filter(User.microsoft_id == profile.get("id")).first()
        print("existing_user",existing_user)
        
        if existing_user:
            # Update existing user details if necessary
            existing_user.email = profile.get("mail", existing_user.email)
            existing_user.name = profile.get("displayName", existing_user.name)
        else:
            # Create a new user if not found
            new_user = User(
                email=profile.get("mail"),
                name=profile.get("displayName"),
                microsoft_id=profile.get("id")
            )
            db.add(new_user)
        
        # Commit changes to the database
        db.commit()
        
        return {"message": "Profile fetched successfully", "profile": profile}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


