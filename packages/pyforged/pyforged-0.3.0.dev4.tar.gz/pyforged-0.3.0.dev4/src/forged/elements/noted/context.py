import contextvars

_current_context = contextvars.ContextVar("issue_context", default={})

def set_issue_context(**kwargs):
    ctx = _current_context.get().copy()
    ctx.update(kwargs)
    _current_context.set(ctx)

def get_issue_context():
    return _current_context.get()
