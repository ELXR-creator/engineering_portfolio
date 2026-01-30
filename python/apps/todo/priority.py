from enum import Enum

class Priority(Enum):
    IMMEDIATE = ("Immediate", 5)
    TODAY = ("Today", 4)
    SOON = ("Soon", 3)
    SCHEDULED = ("Scheduled", 2)
    SOMEDAY = ("Someday", 1)

    def __init__(self, label, weight):
        self.label = label
        self.weight = weight

    def is_urgent(self) -> bool:
        return self.weight >= 4
