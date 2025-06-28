import sqlite3
from typing import List, Dict, Optional


DB_FILE = "feedback.db"


def init_db():
    """Initialize the feedback SQLite DB if not exists."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            sentiment TEXT,
            summary TEXT
        )
        '''
    )
    conn.commit()
    conn.close()


def add_feedback(
    user: Optional[str], message: str,
    sentiment: Optional[str], summary: Optional[str]
) -> int:
    """Insert a feedback entry into the DB."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        '''
        INSERT INTO feedback (user, message, sentiment, summary)
        VALUES (?, ?, ?, ?)
        ''',
        (user, message, sentiment, summary)
    )
    new_id = c.lastrowid
    conn.commit()
    conn.close()
    return new_id


def get_all_feedback() -> List[Dict]:
    """Return all feedback entries as dicts."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        'SELECT id, user, message, created_at, sentiment, summary '
        'FROM feedback ORDER BY created_at DESC'
    )
    rows = c.fetchall()
    conn.close()
    feedback_list = []
    for row in rows:
        feedback_list.append({
            'id': row[0],
            'user': row[1],
            'message': row[2],
            'created_at': row[3],
            'sentiment': row[4],
            'summary': row[5]
        })
    return feedback_list
