import sqlite3
from todo_app import task

connection = sqlite3.connect("todo_app/database/tasks.db")
cursor = connection.cursor()

cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY,
            name TEXT,
            priority INTEGER CHECK (priority BETWEEN 1 AND 3),
            content TEXT,
            due_to DATETIME,
            created_at DATETIME,
            is_done BOOLEAN
        )
        '''
)

def create_new_task(new_task: task.Task) -> None:
    cursor.execute(
        '''
        INSERT INTO tasks (name, priority, content, due_to, created_at,  is_done)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (
            new_task.name,
            new_task.priority,
            new_task.content,
            new_task.due_to,
            new_task.created_at,
            new_task.is_done
        )
    )

def update_priority(task_name: str, priority: int) -> None:
    cursor.execute(
        '''
        UPDATE tasks SET priority = ? WHERE name = ?
        ''',
        (priority, task_name)
    )

def update_content(task_name: str, content: str) -> None:
    cursor.execute(
        '''
        UPDATE tasks SET content = ? WHERE name = ?
        ''',
        (content, task_name)
    )

def mark_as_done(task_name: str) -> None:
    cursor.execute(
        '''
        UPDATE tasks SET is_done = TRUE WHERE name = ?
        ''',
        task_name
    )

def remove_task(task_name: str) -> None:
    cursor.execute(
        '''
        DELETE FROM tasks WHERE name = ?
        ''',
        task_name
    )

def get_list_of_tasks(only_undone: bool = False) -> list[task.Task]|None:
    if only_undone:
        cursor.execute("SELECT * FROM tasks WHERE is_done = FALSE")
    else:
        cursor.execute("SELECT * FROM tasks")
    tasks = []
    for identifier, task_name, priority, content, created_at, due_to, is_done in cursor.fetchall():
        formatted_task = task.Task(
            task_name,
            priority,
            content,
            due_to,
            created_at,
            is_done
        )
        tasks.append(formatted_task)

    return tasks

