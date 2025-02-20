import os
import json
import sqlite3
from invoke import task
from pathlib import Path

@task
def init_db(ctx):
    """Initialize the SQLite database."""
    conn = sqlite3.connect('db.sqlite3')
    print("Database created and connected successfully.")
    conn.close()

@task
def migrate_db(ctx):
    """Run SQL migration files."""
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    migration_files = sorted(os.listdir('db/migrations'))
    for file in migration_files:
        with open(f'db/migrations/{file}', 'r') as f:
            sql = f.read()
            cursor.executescript(sql)
            print(f"Executed {file} successfully.")
    conn.commit()
    conn.close()

@task
def seed_db(ctx):
    """Seed the database with initial data."""
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    with open('db/seeds/french_words_seed.json', 'r') as f:
        words = json.load(f)
        for word in words:
            cursor.execute("INSERT INTO words (french, english) VALUES (?, ?)", (word['french'], word['english']))
            print(f"Inserted {word['french']} - {word['english']} successfully.")
    conn.commit()
    conn.close()
