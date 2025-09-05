import sqlite3
import prepare_database
from todo_app import task

connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

prepare_database.prepare(cursor)


def create_new_task(new_task: task.Task) -> None:
    cursor.execute(
        '''
        INSERT INTO tasks (name, priority, content, created_at, due_to, is_done)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (
            new_task.name,
            new_task.priority,
            new_task.content,
            new_task.created_at,
            new_task.due_to,
            new_task.is_done
        )
    )

def update_priority(task_name: str, priority: int) -> None:
    pass

def update_content(task_name: str, content: str) -> None:
    pass

def mark_as_done(task_name: str) -> None:
    pass

def remove_task(task_name: str) -> None:
    pass