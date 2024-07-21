import sqlite3
from pathlib import Path

CURRENT_DIR = Path(__file__).parent
schema = CURRENT_DIR / "schema.sql"
db = sqlite3.connect("db.sqlite3")
cursor = db.cursor