from priority import Priority
from severity import Severity
from status import Status
from datetime import datetime, timezone

class Task:
    def __init__(
        self,
        name: str,
        description: str,
        status: Status,
        priority: Priority,
        severity: Severity,
        time_given: int
    ):
        self.name = name
        self.description = description
        self.status = status
        self.priority = priority
        self.severity = severity
        self.time_given = time_given
        self.created_at = datetime.now(timezone.utc)
