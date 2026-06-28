"""
LifeQuest AI
AI Game Master Engine
"""

import os
import json

import google.generativeai as genai


class AIGameMaster:
    """
    Generates dynamic game scenarios using Gemini.
    """

    def __init__(self, api_key=None):

        self.api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError("Missing GEMINI_API_KEY")

        genai.configure(api_key=self.api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    # --------------------------------------------------

    def generate_scenario(self, player):

        prompt = f"""
You are the Game Master of LifeQuest AI.

Player Role:
{player.role}

Player Level:
{player.level}

Player Stats:
{player.stats}

Generate ONE realistic life situation.

Return ONLY valid JSON.

Format:

{{
"title":"",
"story":"",
"choices":[
"",
"",
""
],
"effects":[
{{}},
{{}},
{{}}
]
}}

Rules:

- Three choices only.
- Every effect must change stats.

Allowed stats:

Health
Money
Knowledge
Happiness
Reputation
Energy
Experience

Values should be between -20 and +20.

Make it educational and realistic.
"""

        response = self.model.generate_content(prompt)

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "").strip()

        return json.loads(text)
