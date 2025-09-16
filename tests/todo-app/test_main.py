import unittest

from sqlite3 import connect
from datetime import datetime
from todo_app.task import Task
from todo_app.database import database_operations


def make_task(
        title="Test Task",
        priority=1,
        content="Some long content",
        due_to=datetime(2025, 1, 1, 20, 0, 0),
        created_at=datetime(2024, 6, 1, 12, 0, 0, 123456),
        is_done=False
):
    return Task(title, priority, content, due_to, created_at, is_done)

class TestMainApp(unittest.TestCase):
    def setUp(self):
        self.connection = connect(":memory:")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
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
        self.connection.commit()

    def tearDown(self):
        self.connection.close()

    def test_create_new_task_success(self):
        task = make_task()
        database_operations.create_new_task(self.cursor, task)
        self.connection.commit()
        self.cursor.execute("SELECT * FROM tasks WHERE title = ?", (task.title,))
        row = self.cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[1], task.title)
        self.assertEqual(row[2], task.priority)
        self.assertEqual(row[3], task.content)

    def test_create_new_task_validation_error(self):
        with self.assertRaises(ValueError):
            make_task(title="ab")
        with self.assertRaises(ValueError):
            make_task(title="A"*26)
        with self.assertRaises(ValueError):
            make_task(priority=0)
        with self.assertRaises(ValueError):
            make_task(priority=4)
        with self.assertRaises(ValueError):
            make_task(content="short")

    def test_update_priority(self):
        task = make_task()
        database_operations.create_new_task(self.cursor, task)
        self.connection.commit()
        database_operations.update_priority(self.cursor, task.title, 1)
        self.connection.commit()
        self.cursor.execute("SELECT priority FROM tasks WHERE title = ?", (task.title,))
        self.assertEqual(self.cursor.fetchone()[0], 1)

    def test_update_priority_done_task_raises(self):
        task = make_task(is_done=True)
        database_operations.create_new_task(self.cursor, task)
        self.connection.commit()
        with self.assertRaises(ValueError):
            database_operations.update_priority(self.cursor, task.title, 1)

    def test_update_content(self):
        task = make_task()
        database_operations.create_new_task(self.cursor, task)
        self.connection.commit()
        new_content = "This is new valid content!"
        database_operations.update_content(self.cursor, task.title, new_content)
        self.connection.commit()
        self.cursor.execute("SELECT content FROM tasks WHERE title = ?", (task.title,))
        self.assertEqual(self.cursor.fetchone()[0], new_content)

    def test_update_content_done_task_raises(self):
        task = make_task(is_done=True)
        database_operations.create_new_task(self.cursor, task)
        self.connection.commit()
        with self.assertRaises(ValueError):
            database_operations.update_content(self.cursor, task.title, "This is new valid content!")

    def test_mark_as_done(self):
        task = make_task()
        database_operations.create_new_task(self.cursor, task)
        self.connection.commit()
        database_operations.mark_as_done(self.cursor, task.title)
        self.connection.commit()
        self.cursor.execute("SELECT is_done FROM tasks WHERE title = ?", (task.title,))
        self.assertTrue(self.cursor.fetchone()[0])

    def test_mark_as_done_already_done_raises(self):
        task = make_task(is_done=True)
        database_operations.create_new_task(self.cursor, task)
        self.connection.commit()
        with self.assertRaises(ValueError):
            database_operations.mark_as_done(self.cursor, task.title)

    def test_remove_task(self):
        task = make_task()
        database_operations.create_new_task(self.cursor, task)
        self.connection.commit()
        database_operations.remove_task(self.cursor, task.title)
        self.connection.commit()
        self.cursor.execute("SELECT * FROM tasks WHERE title = ?", (task.title,))
        self.assertIsNone(self.cursor.fetchone())

    def test_get_list_of_tasks(self):
        t1 = make_task(title="Title1", is_done=False)
        t2 = make_task(title="Title2", is_done=True)
        t3 = make_task(title="Title3", is_done=False)
        for t in [t1, t2, t3]:
            database_operations.create_new_task(self.cursor, t)
        self.connection.commit()
        all_tasks = database_operations.get_list_of_tasks(self.cursor)
        self.assertEqual(len(all_tasks), 3)
        undone_tasks = database_operations.get_list_of_tasks(self.cursor, only_undone=True)
        titles = [t.title for t in undone_tasks]
        self.assertIn("Title1", titles)
        self.assertIn("Title3", titles)
        self.assertNotIn("Title2", titles)

if __name__ == "__main__":
    unittest.main()