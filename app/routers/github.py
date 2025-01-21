from fastapi import APIRouter, HTTPException
from brain import GithubLoader, GithubDownload

# Initialize the GitHub router
github_router = APIRouter(prefix="/github", tags=["GitHub"])


# POST endpoint to fetch repositories
@github_router.post("/download")
def get_repositories(data: GithubDownload):
    """
    Fetch repositories for a GitHub user.
    - username: GitHub username
    - fetch_private: Whether to include private repositories
    - token: Personal access token for private repository access
    """
    github_loader = GithubLoader(token=data.token)
    github_loader.initalize(username=data.username, fetch_private=data.fetch_private)
    return "Downloading github data"
