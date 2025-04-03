import warnings
from .base import Issue
from .state import maybe_collect
from .types import Severity
from typing import Union, Callable
from forged.elements.noted.exception import IssueException
from .base import Issue

def raise_issue(issue: Union[Issue, Callable[[], Issue]] = None, **kwargs):

    # Lazily create the issue from kwargs if not provided
    if issue is None:
        issue = lambda: Issue(**kwargs)

    if maybe_collect(issue() if not callable(issue) else issue()):
        return

    raise IssueException(issue)


def warn_issue(issue: Issue):
    if maybe_collect(issue):
        return
    warnings.warn(str(issue))
