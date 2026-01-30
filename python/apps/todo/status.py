from enum import Enum

class Status(Enum):
    TODO = ("todo", 1, False)
    IN_PROGRESS = ("in_progress", 2, False)
    BLOCKED = ("blocked", 3, False)
    DONE = ("done", 4, True)
    CANCELLED = ("cancelled", 5, True)

    def __init__(self, label: str, weight: int, is_terminal: bool):
        self.label = label
        self.weight = weight
        self.is_terminal = is_terminal
