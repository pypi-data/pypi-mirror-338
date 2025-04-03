from abc import ABC

from forged.commons.patterns.metadata import Metadata


class PyForgedBase:
    pass

# TODO: add module hooks
class BaseNamespaceItem(ABC, PyForgedBase):
    def __init__(self, name: str = 'default_name'):
        self.name = name
        self.value = None

    pass


class BaseNamespace(ABC, PyForgedBase):
    def __init__(self, ns_name: str = 'root'):
        self.name = ns_name


class BaseIssue:
    def __init__(self,
                 message: str = 'An issue occurred.',
                 kind: str = 'unknown',
                 severity: str = 'warning',
                 origin: str = 'unknown',
                 context: dict | None = None,
                 metadata: dict | Metadata | None = None,
                 hint: str | None = None,
                 tags: list = None
                 ):
        self.message = message

class BaseIssueSolution:
    SEVERITIES = [  # TODO: dynamic loading of custom levels
        'debug',
        'success'
        'info',
        'warning',
        'error',
        'critical'
    ]

    pass


