"""
LifeQuest AI Configuration
"""

APP_NAME = "LifeQuest AI"
APP_TAGLINE = "Every Decision Shapes Your Future"

DEFAULT_ROLE = "Student"

ROLES = [
    "Student",
    "Employee",
    "Farmer",
    "Parent",
    "Officer",
    "Entrepreneur"
]

DEFAULT_STATS = {
    "Health": 100,
    "Money": 100,
    "Knowledge": 50,
    "Happiness": 70,
    "Reputation": 50,
    "Energy": 100,
    "Experience": 0
}

MAX_STAT = 100
MIN_STAT = 0

SCENARIOS_PER_LEVEL = 10

THEME = {
    "primary": "#8B5CF6",      # Purple
    "secondary": "#EC4899",    # Pink
    "accent": "#06B6D4",        # Cyan
    "background": "#09090B",    # Black
    "card": "#18181B",
    "text": "#F8FAFC"
}
