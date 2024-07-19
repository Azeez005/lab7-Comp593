"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from faker import Faker
from datetime import datetime

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: 
    conn=sqlite3.connect(db_path)
    cur=conn.cursor()
    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people 
    (
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL,
    email       TEXT NOT NULL,
    address     TEXT NOT NULL,
    city        TEXT NOT NULL,
    province    TEXT NOT NULL,
    bio         TEXT,
    age         INTEGER,
    created_at  DATETIME NOT NULL,
    updated_at  DATETIME NOT NULL
    );
    """
    cur.execute(create_ppl_tbl_query)
    conn.commit()
    conn.close()

def populate_people_table():
    """Populates the people table with 200 fake people"""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    fake = Faker("en_CA")
    for _ in range(200):
        name = fake.name()
        email = fake.email()
        address = fake.street_address()
        city = fake.city()
        province = fake.administrative_unit()
        bio = fake.text()
        age = fake.random_int(min=20, max=90)

        # Use SQLite function datetime('now') to get current datetime
        cur.execute("""
            INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
            """, (name, email, address, city, province, bio, age))

    conn.commit()
    conn.close()


if __name__ == '__main__':
   main()
