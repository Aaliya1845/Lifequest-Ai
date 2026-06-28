"""
LifeQuest AI
Skill Tree System
"""

from dataclasses import dataclass, field


@dataclass
class Skill:

    name: str

    level: int = 1

    xp: int = 0

    max_level: int = 10

    def add_xp(self, amount):

        self.xp += amount

        while self.xp >= 100 and self.level < self.max_level:

            self.xp -= 100

            self.level += 1


class SkillTree:

    def __init__(self):

        self.skills = {

            "Leadership": Skill("Leadership"),

            "Communication": Skill("Communication"),

            "Finance": Skill("Finance"),

            "Programming": Skill("Programming"),

            "Problem Solving": Skill("Problem Solving"),

            "Critical Thinking": Skill("Critical Thinking"),

            "Agriculture": Skill("Agriculture"),

            "Business": Skill("Business"),

            "Health": Skill("Health"),

            "Creativity": Skill("Creativity")

        }

    # -------------------------------------

    def add_skill_xp(self, skill, xp):

        if skill in self.skills:

            self.skills[skill].add_xp(xp)

    # -------------------------------------

    def get_level(self, skill):

        if skill in self.skills:

            return self.skills[skill].level

        return 1

    # -------------------------------------

    def get_all_skills(self):

        return self.skills

    # -------------------------------------

    def total_level(self):

        return sum(

            skill.level

            for skill in self.skills.values()

        )
