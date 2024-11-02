import sqlite3 as sq
import github_api

conn = sq.connect("github_activity.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS events_table
            (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            event_type TEXT NOT NULL,
            repo_name TEXT NOT NULL,
            event_date TEXT NOT NULL,
            details TEXT
            )
            ''')

conn.commit()

def save_user_activity(username):
    events = github_api.fech_user_git(username)
    save_events(username, events)

def save_events(username, events):
    for event in events:
        with conn:
            cur.execute(''' 
                INSERT INTO events_table(username, event_type, repo_name, event_date, details)
                VALUES (?, ?, ?, ?, ?)
            ''', (username, event['event_type'], event['repo_name'], event['event_date'], event['details']))

def get_last_user_events(username, limit = 10):
    with conn:
        cur.execute('''
            SELECT event_type, repo_name, event_date, details
            FROM events_table
            WHERE username = ?
            ORDER BY event_date DESC
            LIMIT ?
        ''',(username, limit))

        last_user_events = cur.fetchall()

    return last_user_events

def get_all_user_events(username):
    with conn:
        cur.execute('''
            SELECT event_type, repo_name, event_date, details
            FROM events_table
            WHERE username = ?
            ORDER BY event_date DESC
        ''',(username,))
        
        all_user_events = cur.fetchall()

    return all_user_events
