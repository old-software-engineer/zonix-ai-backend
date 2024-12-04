from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.common.database import Base, engine
from app.routes.graph import router as graph_router
from app.routes.auth import router as auth_router

# Initialize FastAPI app
app = FastAPI(
    title="Your API",
    description="API with CORS Support",
    version="1.0.0",
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(graph_router, prefix="/graph", tags=["Microsoft Graph API"])