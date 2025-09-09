import datetime
import sqlite3
from todo_app import task

connection = sqlite3.connect("todo_app/database/tasks.db")
cursor = connection.cursor()

cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks(
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

def create_new_task(new_task: task.Task) -> None:
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

def update_priority(title: str, priority: int) -> None:
    cursor.execute(
        '''
        SELECT * FROM tasks WHERE title = ?
        ''',
        (title,)
    )
    found_task = cursor.fetchone()
    if found_task and found_task.is_done == False:
        cursor.execute(
            '''
            UPDATE tasks SET priority = ? WHERE title = ?
            ''',
            (priority, title)
        )
    else:
        raise ValueError("You cannot modify tasks, which are done") # TODO: przemyśleć, czy napewdo dobry wybór errora

def update_content(title: str, content: str) -> None:
    cursor.execute(
        '''
        SELECT *
        FROM tasks
        WHERE title = ?
        ''',
        (title,)
    )
    found_task = cursor.fetchone()
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
        raise ValueError("You cannot modify tasks, which are done")


def mark_as_done(title: str) -> None:
    cursor.execute(
        '''
        SELECT *
        FROM tasks
        WHERE title = ?
        ''',
        (title,)
    )
    found_task = cursor.fetchone()
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

def remove_task(title: str) -> None:
    cursor.execute(
        '''
        DELETE FROM tasks WHERE title = ?
        ''',
        (title,)
    )

def get_list_of_tasks(only_undone: bool = False) -> list[task.Task]|None:
    if only_undone:
        cursor.execute("SELECT * FROM tasks WHERE is_done = FALSE")
    else:
        cursor.execute("SELECT * FROM tasks")
    tasks = []
    for identifier, title, priority, content, due_to, created_at,  is_done in cursor.fetchall():
        formatted_task = task.Task(
            title,
            priority,
            content,
            datetime.datetime.strptime(due_to, "%Y-%m-%d %H:%M:%S"),
            datetime.datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S.%f"),
            bool(is_done)
        )
        tasks.append(formatted_task)

    return tasks

