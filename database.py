"""
LifeQuest AI
Database Manager
SQLite Save System
"""

import sqlite3
import json
from typing import Optional


class DatabaseManager:

    def __init__(self, db_name="lifequest.db"):

        self.conn = sqlite3.connect(
            db_name,
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.create_tables()

    # -------------------------------------------------
    # Create Database Tables
    # -------------------------------------------------

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS players(

            name TEXT PRIMARY KEY,

            role TEXT,

            level INTEGER,

            stats TEXT,

            achievements TEXT,

            completed INTEGER

        )
        """)

        self.conn.commit()

    # -------------------------------------------------
    # Save Player
    # -------------------------------------------------

    def save_player(self, player):

        self.cursor.execute("""

        INSERT OR REPLACE INTO players
        VALUES (?,?,?,?,?,?)

        """, (

            player.name,

            player.role,

            player.level,

            json.dumps(player.stats),

            json.dumps(player.achievements),

            player.completed_scenarios

        ))

        self.conn.commit()

    # -------------------------------------------------
    # Load Player
    # -------------------------------------------------

    def load_player(self, name: str):

        self.cursor.execute(

            "SELECT * FROM players WHERE name=?",

            (name,)

        )

        row = self.cursor.fetchone()

        if row is None:

            return None

        return {

            "name": row[0],

            "role": row[1],

            "level": row[2],

            "stats": json.loads(row[3]),

            "achievements": json.loads(row[4]),

            "completed": row[5]

        }

    # -------------------------------------------------
    # All Players
    # -------------------------------------------------

    def get_all_players(self):

        self.cursor.execute(

            "SELECT name,role,level FROM players"

        )

        return self.cursor.fetchall()

    # -------------------------------------------------
    # Delete Save
    # -------------------------------------------------

    def delete_player(self, name):

        self.cursor.execute(

            "DELETE FROM players WHERE name=?",

            (name,)

        )

        self.conn.commit()

    # -------------------------------------------------
    # Close
    # -------------------------------------------------

    def close(self):

        self.conn.close()
