"""
LifeQuest AI
Universal AI Engine
"""

import os
import random
import json

from scenarios import SCENARIOS

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except Exception:
    GEMINI_AVAILABLE = False


class AIEngine:

    def __init__(self):

        self.api_key = os.getenv("GEMINI_API_KEY")

        self.available = False

        if GEMINI_AVAILABLE and self.api_key:

            try:

                genai.configure(api_key=self.api_key)

                self.model = genai.GenerativeModel(
                    "gemini-2.5-flash"
                )

                self.available = True

            except Exception:

                self.available = False

    # ------------------------------------

    def local_scenario(self, role):

        return random.choice(
            SCENARIOS[role]
        )

    # ------------------------------------

    def ai_scenario(self, player):

        prompt = f"""

Generate ONE realistic scenario.

Role:

{player.role}

Stats:

{player.stats}

Return JSON only.

"""

        try:

            response = self.model.generate_content(prompt)

            text = response.text.strip()

            text = text.replace(
                "```json",
                ""
            ).replace(
                "```",
                ""
            )

            return json.loads(text)

        except Exception:

            return None

    # ------------------------------------

    def generate(self, player):

        if self.available:

            scenario = self.ai_scenario(player)

            if scenario:

                return scenario

        return self.local_scenario(
            player.role
        )
