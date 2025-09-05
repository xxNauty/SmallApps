import sqlite3

def prepare(cursor: sqlite3.Cursor):
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY,
            name TEXT,
            priority INTEGER CHECK (priority BETWEEN 1 AND 3),
            content TEXT,
            created_at DATETIME,
            due_to DATETIME,
            is_done BOOLEAN
        )
        '''
    )