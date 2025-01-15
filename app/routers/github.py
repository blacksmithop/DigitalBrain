from fastapi import APIRouter, HTTPException
from brain import Github, GithubDownload
import requests

# Initialize the GitHub router
github_router = APIRouter(prefix="/github", tags=["GitHub"])


# Helper function to fetch repositories
def fetch_repositories(username: str, fetch_private: bool, token: str = None):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {}

    if token:
        headers["Authorization"] = f"Bearer {token}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        if fetch_private:
            return [repo for repo in repos if repo.get("private", False)]
        return [repo for repo in repos if not repo.get("private", False)]
    else:
        raise HTTPException(status_code=response.status_code, detail=response.json())

# POST endpoint to fetch repositories
@github_router.post("/download")
def get_repositories(data: GithubDownload):
    """
    Fetch repositories for a GitHub user.
    - username: GitHub username
    - fetch_private: Whether to include private repositories
    - token: Personal access token for private repository access
    """
    github_loader = Github(token=data.token)
    github_loader.initalize(username=data.username, fetch_private=data.fetch_private)
    return "Downloading github data"
