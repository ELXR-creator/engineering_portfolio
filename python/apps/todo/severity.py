from enum import Enum

class Severity(Enum):
    LIFE_CRITICAL = ("Life Critical", 5)      # Skipping causes serious long-term damage
    IDENTITY_LEVEL = ("Identity Level", 4)    # Shapes who you become (habits, discipline)
    GROWTH_IMPACT = ("Growth Impact", 3)      # Strongly affects progress
    MAINTENANCE = ("Maintenance", 2)          # Keeps things stable
    OPTIONAL = ("Optional", 1)                # No real downside

    def __init__(self, label: str, weight: int):
        self.label = label
        self.weight = weight
