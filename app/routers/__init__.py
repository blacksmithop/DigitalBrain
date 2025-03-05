from .github import github_router
from .medium import medium_router
from .notion import notion_router

router_list = [github_router, medium_router, notion_router]