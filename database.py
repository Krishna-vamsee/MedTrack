# database.py
import sqlite3
import os
from datetime import datetime

# ------------------ Paths ------------------
DATA_DIR = "data"
DB_PATH = os.path.join(DATA_DIR, "medicines.db")

# ------------------ Helper Functions ------------------
def ensure_dirs():
    """Ensure data folder exists"""
    os.makedirs(DATA_DIR, exist_ok=True)

def get_conn():
    """Connect to SQLite database"""
    return sqlite3.connect(DB_PATH)

# ------------------ Main Database Functions ------------------
def init_db():
    """Initialize the database if not created"""
    ensure_dirs()
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS medicines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                dosage TEXT NOT NULL,
                time TEXT NOT NULL,
                status TEXT DEFAULT 'Pending'
            );
        """)
        conn.commit()

def add_medicine(name, dosage, at_time):
    """Add a new medicine to the schedule"""
    try:
        datetime.strptime(at_time, "%H:%M")
    except ValueError:
        print("Time must be in HH:MM 24-hour format (e.g:, 09:00 or 21:30).")
        return False
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO medicines (name, dosage, time) VALUES (?, ?, ?)",
                    (name.strip(), dosage.strip(), at_time.strip()))
        conn.commit()
    return True

def view_medicines():
    """Return a list of all medicines"""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name, dosage, time, status FROM medicines ORDER BY time;")
        return cur.fetchall()

def delete_medicine(med_id):
    """Delete a medicine by ID"""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM medicines WHERE id=?;", (med_id,))
        conn.commit()

def mark_taken(med_id):
    """Mark a medicine as Taken"""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("UPDATE medicines SET status='Taken' WHERE id=?;", (med_id,))
        conn.commit()

def reset_statuses():
    """Reset all medicine statuses to Pending"""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("UPDATE medicines SET status='Pending';")
        conn.commit()

# ------------------ Reset / Clear Options ------------------
def clear_all_medicines():
    """Delete all medicine records but keep the table"""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM medicines;")
        conn.commit()
    print("All medicine records have been cleared.")

def reset_database():
    """Drop the medicines table and recreate it"""
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS medicines;")
        conn.commit()
    init_db()
    print("Database has been reset to empty state.")
