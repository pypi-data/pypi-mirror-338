from github_contexts.github.context import GitHubContext
from github_contexts.github import enum, payload
from github_contexts import _util

def create(context: dict, pop_token: bool = True) -> GitHubContext:
    """Create a GitHub context object from the given dictionary."""
    context_normalized = _util.normalize_newlines(context)
    return GitHubContext(context_normalized, pop_token=pop_token)
