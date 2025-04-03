"""
Systematic way to catch, wrap, or propagate errors.

**Used for:**

- Central error mapping,
- Retry logic,
- Graceful degradation

**Tools include:**

- tenacity,
- custom exception hierarchies,
- error middleware
"""
from .hooks import install_hooks

from .base import Issue
from .emit import raise_issue, warn_issue
from .types import Severity, Kind
from .context import set_issue_context, get_issue_context

__all__ = [
    "Issue",
    "raise_issue",
    "warn_issue",
    "Severity",
    "Kind",
    "set_issue_context",
    "get_issue_context",
]
