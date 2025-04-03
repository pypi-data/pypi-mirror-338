import sys
import warnings
from .base import Issue
from .types import Severity, Kind
from forged.elements.noted.exception import IssueException

def install_hooks():
    sys.excepthook = excepthook
    warnings.showwarning = showwarning

def excepthook(exc_type, exc_value, traceback):
    if isinstance(exc_value, IssueException):
        issue = exc_value.issue
    else:
        issue = Issue(
            message=str(exc_value),
            severity=Severity.ERROR,
            kind=Kind.RUNTIME,
            context={"type": exc_type.__name__}
        )
    print("[EXCEPTION]", issue)

def showwarning(message, category, filename, lineno, file=None, line=None):
    issue = Issue(
        message=str(message),
        severity=Severity.WARNING,
        kind=Kind.RUNTIME,
        context={"file": filename, "line": lineno}
    )
    print("[WARNING]", issue)
