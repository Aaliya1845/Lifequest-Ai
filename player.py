"""
LifeQuest AI
Player Model
"""

from dataclasses import dataclass, field
from typing import Dict, List
from inventory import Inventory

from config import DEFAULT_STATS, MAX_STAT, MIN_STAT


@dataclass
class Player:
    name: str
    role: str

    stats: Dict[str, int] = field(
        default_factory=lambda: DEFAULT_STATS.copy()
        inventory: Inventory = field(default_factory=Inventory)
        
    )

    level: int = 1
    achievements: List[str] = field(default_factory=list)
    completed_scenarios: int = 0

    # -------------------------
    # Update Stats
    # -------------------------
    def update_stats(self, changes: Dict[str, int]):
        """
        Update player statistics safely.
        """

        for stat, value in changes.items():

            if stat not in self.stats:
                continue

            if stat == "Experience":
                self.stats[stat] += value
                continue

            self.stats[stat] = max(
                MIN_STAT,
                min(MAX_STAT, self.stats[stat] + value)
            )

        self._check_level_up()

    # -------------------------
    # Level System
    # -------------------------
    def _check_level_up(self):

        xp = self.stats["Experience"]

        new_level = (xp // 100) + 1

        if new_level > self.level:
            self.level = new_level

    # -------------------------
    # Achievement
    # -------------------------
    def unlock(self, achievement: str):

        if achievement not in self.achievements:
            self.achievements.append(achievement)

    # -------------------------
    # Scenario Counter
    # -------------------------
    def complete_scenario(self):

        self.completed_scenarios += 1

        self.update_stats({
            "Experience": 10
        })

    # -------------------------
    # Dashboard Data
    # -------------------------
    def dashboard(self):

        return {
            "Name": self.name,
            "Role": self.role,
            "Level": self.level,
            "Stats": self.stats,
            "Achievements": self.achievements,
            "Completed": self.completed_scenarios
        }
