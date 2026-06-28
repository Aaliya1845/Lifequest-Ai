"""
LifeQuest AI
Database Manager v2.0
"""

import sqlite3
import json


class DatabaseManager:

    def __init__(self, db_name="lifequest.db"):

        self.conn = sqlite3.connect(
            db_name,
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.create_tables()

    # ----------------------------------------------------
    # Create Tables
    # ----------------------------------------------------

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS players(

            name TEXT PRIMARY KEY,

            role TEXT,

            level INTEGER,

            completed INTEGER,

            player_data TEXT

        )

        """)

        self.conn.commit()

    # ----------------------------------------------------
    # Convert Player -> JSON
    # ----------------------------------------------------

    def player_to_json(self, player):

        data = {

            "name": player.name,

            "role": player.role,

            "level": player.level,

            "completed": player.completed_scenarios,

            "stats": player.stats,

            "achievements": player.achievements,

            "inventory": player.inventory.get_items(),

            "skills": {}

        }

        for name, skill in player.skills.get_all_skills().items():

            data["skills"][name] = {

                "level": skill.level,

                "xp": skill.xp

            }

        return json.dumps(data)

    # ----------------------------------------------------
    # Save Player
    # ----------------------------------------------------

    def save_player(self, player):

        json_data = self.player_to_json(player)

        self.cursor.execute("""

        INSERT OR REPLACE INTO players
        VALUES(?,?,?,?,?)

        """, (

            player.name,

            player.role,

            player.level,

            player.completed_scenarios,

            json_data

        ))

        self.conn.commit()

    # ----------------------------------------------------
    # Load Player
    # ----------------------------------------------------

    def load_player(self, player_name):

        self.cursor.execute(

            "SELECT player_data FROM players WHERE name=?",

            (player_name,)

        )

        row = self.cursor.fetchone()

        if row is None:

            return None

        return json.loads(row[0])

    # ----------------------------------------------------
    # Check Save Exists
    # ----------------------------------------------------

    def exists(self, player_name):

        self.cursor.execute(

            "SELECT name FROM players WHERE name=?",

            (player_name,)

        )

        return self.cursor.fetchone() is not None
        # ----------------------------------------------------
    # List All Players
    # ----------------------------------------------------

    def get_all_players(self):

        self.cursor.execute("""

        SELECT
            name,
            role,
            level,
            completed

        FROM players

        ORDER BY level DESC

        """)

        return self.cursor.fetchall()

    # ----------------------------------------------------
    # Delete Player
    # ----------------------------------------------------

    def delete_player(self, player_name):

        self.cursor.execute(

            "DELETE FROM players WHERE name=?",

            (player_name,)

        )

        self.conn.commit()

    # ----------------------------------------------------
    # Export Save
    # ----------------------------------------------------

    def export_player(self, player_name):

        data = self.load_player(player_name)

        if data is None:
            return None

        return json.dumps(
            data,
            indent=4
        )

    # ----------------------------------------------------
    # Import Save
    # ----------------------------------------------------

    def import_player(self, json_string):

        data = json.loads(json_string)

        self.cursor.execute("""

        INSERT OR REPLACE INTO players
        VALUES(?,?,?,?,?)

        """, (

            data["name"],

            data["role"],

            data["level"],

            data["completed"],

            json.dumps(data)

        ))

        self.conn.commit()

    # ----------------------------------------------------
    # Player Count
    # ----------------------------------------------------

    def player_count(self):

        self.cursor.execute(

            "SELECT COUNT(*) FROM players"

        )

        return self.cursor.fetchone()[0]

    # ----------------------------------------------------
    # Database Info
    # ----------------------------------------------------

    def database_info(self):

        return {

            "players": self.player_count(),

            "database": "lifequest.db",

            "version": "2.0"

        }

    # ----------------------------------------------------
    # Close Database
    # ----------------------------------------------------

    def close(self):

        if self.conn:

            self.conn.close()
