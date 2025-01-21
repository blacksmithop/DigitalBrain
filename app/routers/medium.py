from fastapi import APIRouter, HTTPException
from brain import MediumLoader, MediumDownload

# Initialize the GitHub router
medium_router = APIRouter(prefix="/medium", tags=["Medium"])

# POST endpoint to fetch repositories
@medium_router.post("/download")
def get_repositories(data: MediumDownload):
    """
    Fetch articles for a Medium user.
    - username: Medium username
    """
    medium_loader = MediumLoader()
    medium_loader.initalize(username=data.username)
    return "Downloading medium data"
