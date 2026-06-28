"""
LifeQuest AI
Game Engine
"""

import random

from player import Player
from scenarios import SCENARIOS


class GameEngine:

    def __init__(self, player: Player):
        self.player = player
        self.current_scenario = None

    # ----------------------------------------
    # Get a random scenario for player's role
    # ----------------------------------------
    def next_scenario(self):

        role = self.player.role

        if role not in SCENARIOS:
            return None

        self.current_scenario = random.choice(
            SCENARIOS[role]
        )

        return self.current_scenario

    # ----------------------------------------
    # Apply player's choice
    # ----------------------------------------
    def choose(self, choice_index: int):

        if self.current_scenario is None:
            return {
                "success": False,
                "message": "No scenario loaded."
            }

        try:

            effects = self.current_scenario["effects"][choice_index]

            self.player.update_stats(effects)

            self.player.complete_scenario()

            achievements = self.check_achievements()

            return {
                "success": True,
                "effects": effects,
                "achievements": achievements
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }

    # ----------------------------------------
    # Achievement System
    # ----------------------------------------
    def check_achievements(self):

        unlocked = []

        stats = self.player.stats

        # Knowledge Master
        if stats["Knowledge"] >= 80:
            self.player.unlock("📚 Knowledge Master")
            unlocked.append("📚 Knowledge Master")

        # Rich Player
        if stats["Money"] >= 150:
            self.player.unlock("💰 Wealth Builder")
            unlocked.append("💰 Wealth Builder")

        # Happy Life
        if stats["Happiness"] >= 90:
            self.player.unlock("😊 Happy Life")
            unlocked.append("😊 Happy Life")

        # Community Hero
        if stats["Reputation"] >= 80:
            self.player.unlock("⭐ Community Hero")
            unlocked.append("⭐ Community Hero")

        # Experienced
        if self.player.level >= 5:
            self.player.unlock("🏆 Experienced Leader")
            unlocked.append("🏆 Experienced Leader")

        return unlocked

    # ----------------------------------------
    # Dashboard
    # ----------------------------------------
    def dashboard(self):

        return {
            "player": self.player.dashboard(),
            "scenario": self.current_scenario
        }
