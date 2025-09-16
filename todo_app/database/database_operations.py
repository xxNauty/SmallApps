from datetime import datetime
from todo_app.task import Task
from sqlite3 import Cursor, connect

def init_database() -> Cursor:
    connection = connect("todo_app/database/tasks.db")
    cursor = connection.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks
        (
            id INTEGER PRIMARY KEY,
            title TEXT CHECK (length(title) BETWEEN 3 AND 25),
            priority INTEGER CHECK (priority BETWEEN 1 AND 3),
            content TEXT CHECK (length(content) >= 10),
            due_to DATETIME,
            created_at DATETIME,
            is_done BOOLEAN
        )
        '''
    )
    return cursor

def create_new_task(cursor: Cursor, new_task: Task) -> None:
    cursor.execute(
        '''
        INSERT INTO tasks (title, priority, content, due_to, created_at,  is_done)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (
            new_task.title,
            new_task.priority,
            new_task.content,
            new_task.due_to,
            new_task.created_at,
            new_task.is_done
        )
    )

def update_priority(cursor: Cursor, title: str, priority: int) -> None:
    cursor.execute(
        '''
        SELECT * FROM tasks WHERE title = ?
        ''',
        (title,)
    )
    found_task = cursor.fetchone()
    found_task = Task.from_tuple(found_task)

    if found_task and found_task.is_done == False:
        cursor.execute(
            '''
            UPDATE tasks SET priority = ? WHERE title = ?
            ''',
            (priority, title)
        )
    else:
        raise PermissionError("You cannot modify tasks, which are done")

def update_content(cursor: Cursor, title: str, content: str) -> None:
    cursor.execute(
        '''
        SELECT *
        FROM tasks
        WHERE title = ?
        ''',
        (title,)
    )
    found_task = cursor.fetchone()
    found_task = Task.from_tuple(found_task)

    if found_task and found_task.is_done == False:
        cursor.execute(
            '''
            UPDATE tasks
            SET content = ?
            WHERE title = ?
            ''',
            (content, title)
        )
    else:
        raise PermissionError("You cannot modify tasks, which are done")


def mark_as_done(cursor: Cursor, title: str) -> None:
    cursor.execute(
        '''
        SELECT *
        FROM tasks
        WHERE title = ?
        ''',
        (title,)
    )
    found_task = cursor.fetchone()
    found_task = Task.from_tuple(found_task)
    if found_task and found_task.is_done == False:
        cursor.execute(
            '''
            UPDATE tasks
            SET is_done = TRUE
            WHERE title = ?
            ''',
            (title,)  # ZAJEBIŚCIE WAŻNE, INACZEJ STRING TRAKTOWANY BĘDZIE JAKO LISTA ZNAKÓW
        )
    else:
        raise ValueError("You cannot modify tasks, which are done")

def remove_task(cursor: Cursor, title: str) -> None:
    cursor.execute(
        '''
        DELETE FROM tasks WHERE title = ?
        ''',
        (title,)
    )

def get_list_of_tasks(cursor: Cursor, only_undone: bool = False) -> list[Task]|None:
    if only_undone:
        cursor.execute("SELECT * FROM tasks WHERE is_done = FALSE")
    else:
        cursor.execute("SELECT * FROM tasks")
    tasks = []
    for identifier, title, priority, content, due_to, created_at,  is_done in cursor.fetchall():
        formatted_task = Task(
            title,
            priority,
            content,
            datetime.strptime(due_to, "%Y-%m-%d %H:%M:%S"),
            datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S.%f"),
            bool(is_done)
        )
        tasks.append(formatted_task)

    return tasks

