"""
LifeQuest AI
Player Model
"""

from dataclasses import dataclass, field
from typing import Dict, List

from config import DEFAULT_STATS, MAX_STAT, MIN_STAT
from inventory import Inventory
from skill_tree import SkillTree


@dataclass
class Player:
    name: str
    role: str

    stats: Dict[str, int] = field(
        default_factory=lambda: DEFAULT_STATS.copy()
    )

    level: int = 1

    achievements: List[str] = field(default_factory=list)

    completed_scenarios: int = 0

    inventory: Inventory = field(default_factory=Inventory)

    skills: SkillTree = field(default_factory=SkillTree)

    def __post_init__(self):
        """Give each role a starter item."""

        starter_items = {
            "Student": "📚 Notebook",
            "Employee": "💼 Office Bag",
            "Farmer": "🌱 Seed Pack",
            "Parent": "🏠 Family Planner",
            "Officer": "📻 Radio",
            "Entrepreneur": "💳 Business Card",
        }

        item = starter_items.get(self.role)

        if item and not self.inventory.has_item(item):
            self.inventory.add_item(item)

    # --------------------------------------------------
    # Update Stats
    # --------------------------------------------------

    def update_stats(self, changes: Dict[str, int]):

        for stat, value in changes.items():

            if stat not in self.stats:
                continue

            if stat == "Experience":
                self.stats[stat] += value
                continue

            self.stats[stat] = max(
                MIN_STAT,
                min(
                    MAX_STAT,
                    self.stats[stat] + value
                )
            )

        self._check_level_up()

    # --------------------------------------------------
    # Level System
    # --------------------------------------------------

    def _check_level_up(self):

        xp = self.stats["Experience"]

        self.level = (xp // 100) + 1

    # --------------------------------------------------
    # Achievement
    # --------------------------------------------------

    def unlock(self, achievement: str):

        if achievement not in self.achievements:
            self.achievements.append(achievement)

    # --------------------------------------------------
    # Scenario Completed
    # --------------------------------------------------

    def complete_scenario(self):

        self.completed_scenarios += 1

        self.update_stats({
            "Experience": 10
        })

    # --------------------------------------------------
    # Inventory
    # --------------------------------------------------

    def add_item(self, item, quantity=1):

        self.inventory.add_item(item, quantity)

    def remove_item(self, item, quantity=1):

        return self.inventory.remove_item(item, quantity)

    # --------------------------------------------------
    # Skills
    # --------------------------------------------------

    def add_skill_xp(self, skill, xp):

        self.skills.add_skill_xp(skill, xp)

    # --------------------------------------------------
    # Dashboard Data
    # --------------------------------------------------

    def dashboard(self):

        return {
            "Name": self.name,
            "Role": self.role,
            "Level": self.level,
            "Stats": self.stats,
            "Achievements": self.achievements,
            "Completed": self.completed_scenarios,
            "Inventory": self.inventory.get_items(),
            "Skills": {
                name: {
                    "level": skill.level,
                    "xp": skill.xp
                }
                for name, skill in self.skills.get_all_skills().items()
            }
        }
