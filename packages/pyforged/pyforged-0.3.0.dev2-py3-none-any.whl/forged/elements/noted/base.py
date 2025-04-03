from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Optional
from forged.elements.noted.types import Severity, Kind

@dataclass
class Issue:
    message: str
    kind: Kind = Kind.GENERAL
    severity: Severity = Severity.ERROR
    context: Dict[str, Any] = field(default_factory=dict)
    hint: Optional[str] = None
    solution: Optional[str] = None
    code: Optional[str] = None
    tags: list[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.utcnow)
    origin: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "message": self.message,
            "kind": self.kind,
            "severity": self.severity,
            "context": self.context,
            "hint": self.hint,
            "solution": self.solution,
            "code": self.code,
            "tags": self.tags,
            "timestamp": self.timestamp.isoformat(),
            "origin": self.origin,
        }

    def __str__(self):
        return f"[{self.severity}] {self.kind}: {self.message}"
