import contextlib
import contextvars

_collected_issues = contextvars.ContextVar("collected_issues", default=None)

@contextlib.contextmanager
def collect_issues():
    issues = []
    token = _collected_issues.set(issues)
    try:
        yield issues
    finally:
        _collected_issues.reset(token)

def maybe_collect(issue: Issue):
    current = _collected_issues.get()
    if current is not None:
        current.append(issue)
        return True
    return False
