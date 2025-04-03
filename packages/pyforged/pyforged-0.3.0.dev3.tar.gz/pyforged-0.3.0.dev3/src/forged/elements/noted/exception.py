class IssueException(Exception):
    """Exception wrapping a structured Issue object, lazily if needed."""

    def __init__(self, issue_or_factory):
        self._issue = issue_or_factory
        self._resolved = None
        super().__init__(self._get_message())

    def _get_message(self):
        return str(self.issue)

    @property
    def issue(self):
        if self._resolved is None:
            if callable(self._issue):
                self._resolved = self._issue()
            else:
                self._resolved = self._issue
        return self._resolved