from brain import GITHUB_TOKEN
from requests import get, exceptions
from git import Repo
from os import path, makedirs
from brain.models import GithubRepo
from typing import List, Optional
from rich.progress import Progress
from rich.console import Console

console = Console()


class GithubLoader:
    def __init__(self, token: Optional[str] = None):
        self.user_authenticated = False

        if token:
            self.user_authenticated = True
            self.headers = {"Authorization": f"token {token}"}
        else:
            self.headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    def initalize(self, username: str, fetch_private=False):
        if self.user_authenticated != True:
            fetch_private = False
        user_repos: List[GithubRepo] = self.list_user_repos(
            username=username, fetch_private=fetch_private
        )
        self.clone_repositories(repos=user_repos)

    def list_user_repos(self, username, fetch_private=False):
        """
        List repositories for a given GitHub user.

        :param user: GitHub username
        :param token: GitHub personal access token (default: None)
        :param fetch_private: Flag to fetch private repositories (default: False)
        :return: List of repository names
        """
        url = f"https://api.github.com/users/{username}/repos"

        params = {"visibility": "all" if fetch_private else "public"}

        try:
            response = get(url, headers=self.headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            repos = response.json()
            return [GithubRepo(**item) for item in repos]

        except exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return []

    def clone_repositories(
    self, repos: List[GithubRepo], target_directory: str = "./hippocampus/github"
    ):
        """
        Clone the given repositories into a target directory.

        :param repos: List of GithubRepo objects
        :param target_directory: Directory to clone the repositories into
        """
        if not path.exists(target_directory):
            makedirs(target_directory)

        with Progress(console=console) as progress:
            clone_task = progress.add_task("[green]Cloning repositories...", total=len(repos))

            for repo in repos:
                repo_path = path.join(target_directory, repo.name)
                if not path.exists(repo_path):
                    try:
                        progress.console.print(
                            f"Cloning [cyan]{repo.name}[/cyan] into [yellow]{repo_path}[/yellow]..."
                        )
                        Repo.clone_from(repo.clone_url, repo_path, depth=1)
                        progress.console.print(
                            f"[green]Successfully cloned[/green] [cyan]{repo.name}[/cyan]"
                        )
                    except Exception as e:
                        progress.console.print(
                            f"[red]Failed to clone[/red] [cyan]{repo.name}[/cyan] due to [red]{e}[/red]"
                        )
                else:
                    progress.console.print(
                        f"Repository [cyan]{repo.name}[/cyan] already exists in [yellow]{target_directory}[/yellow]"
                    )

                progress.update(clone_task, advance=1)


if __name__ == "__main__":

    gh = Github()
    print(gh.list_user_repos(username="blacksmithop"))
