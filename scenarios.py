"""
LifeQuest AI
Scenario Library
"""

SCENARIOS = {

    "Student": [

        {
            "title": "Exam Tomorrow",

            "story":
            "Your final exam is tomorrow, but your friends invite you to a late-night party.",

            "choices": [
                "Study all evening",
                "Go to the party",
                "Study for two hours then relax"
            ],

            "effects": [
                {
                    "Knowledge": 15,
                    "Happiness": -5,
                    "Energy": -10,
                    "Experience": 10
                },
                {
                    "Knowledge": -10,
                    "Happiness": 15,
                    "Energy": -20,
                    "Experience": 5
                },
                {
                    "Knowledge": 8,
                    "Happiness": 8,
                    "Energy": -5,
                    "Experience": 8
                }
            ]
        },

        {
            "title": "Online Course",

            "story":
            "A free AI course is available, but it takes two hours every day.",

            "choices": [
                "Join the course",
                "Ignore it",
                "Save it for later"
            ],

            "effects": [
                {
                    "Knowledge": 20,
                    "Energy": -10,
                    "Experience": 15
                },
                {
                    "Knowledge": -5,
                    "Experience": 0
                },
                {
                    "Knowledge": 5,
                    "Experience": 3
                }
            ]
        }

    ],

    "Farmer": [

        {
            "title": "Unexpected Rain",

            "story":
            "Heavy rainfall is predicted tomorrow.",

            "choices": [
                "Harvest today",
                "Wait",
                "Cover crops"
            ],

            "effects": [
                {
                    "Money": 20,
                    "Experience": 10
                },
                {
                    "Money": -15,
                    "Experience": 3
                },
                {
                    "Money": 8,
                    "Knowledge": 5,
                    "Experience": 8
                }
            ]
        }

    ],

    "Employee": [

        {
            "title": "Office Deadline",

            "story":
            "Your manager asks for urgent work while your teammate needs help.",

            "choices": [
                "Finish your task",
                "Help teammate",
                "Balance both"
            ],

            "effects": [
                {
                    "Reputation": 5,
                    "Experience": 10
                },
                {
                    "Reputation": 10,
                    "Energy": -10
                },
                {
                    "Reputation": 8,
                    "Experience": 8
                }
            ]
        }

    ],

    "Parent": [

        {
            "title": "Weekend Choice",

            "story":
            "Your child wants to play while homework is unfinished.",

            "choices": [
                "Homework first",
                "Play first",
                "Split time"
            ],

            "effects": [
                {
                    "Reputation": 5,
                    "Knowledge": 5
                },
                {
                    "Happiness": 15,
                    "Knowledge": -5
                },
                {
                    "Happiness": 8,
                    "Knowledge": 5
                }
            ]
        }

    ],

    "Officer": [

        {
            "title": "Flood Warning",

            "story":
            "Heavy flooding is expected in nearby villages.",

            "choices": [
                "Evacuate immediately",
                "Wait for confirmation",
                "Send rescue team only"
            ],

            "effects": [
                {
                    "Reputation": 20,
                    "Experience": 20
                },
                {
                    "Reputation": -15
                },
                {
                    "Reputation": 8,
                    "Experience": 8
                }
            ]
        }

    ],

    "Entrepreneur": [

        {
            "title": "Investor Meeting",

            "story":
            "An investor offers funding but wants 40% ownership.",

            "choices": [
                "Accept",
                "Reject",
                "Negotiate"
            ],

            "effects": [
                {
                    "Money": 25,
                    "Reputation": 5
                },
                {
                    "Money": -10,
                    "Experience": 5
                },
                {
                    "Money": 15,
                    "Reputation": 10,
                    "Experience": 15
                }
            ]
        }

    ]

}
