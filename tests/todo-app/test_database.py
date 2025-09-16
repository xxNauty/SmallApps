import unittest

from sqlite3 import connect
from datetime import datetime
from todo_app.task import Task
from todo_app.database import database_operations


class TestTodoAppDatabase(unittest.TestCase):
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

    def tearDown(self):
        self.connection.close()

    @staticmethod
    def make_task(
            title="Test Task",
            priority=1,
            content="Some long content",
            due_to=datetime(2025, 1, 1, 20, 0, 0),
            created_at=datetime(2024, 6, 1, 12, 0, 0, 123456),
            is_done=False
    ):
        return Task(title, priority, content, due_to, created_at, is_done)

    def insert_task(self, tsk=None):
        tsk = tsk or self.make_task()
        self.cursor.execute(
            '''
            INSERT INTO tasks (title, priority, content, due_to, created_at, is_done)
            VALUES (?, ?, ?, ?, ?, ?)
            ''',
            (
                tsk.title,
                tsk.priority,
                tsk.content,
                tsk.due_to,
                tsk.created_at,
                tsk.is_done
            )
        )
        self.connection.commit()
        return tsk

    def test_create_new_task(self):
        tsk = self.make_task()
        database_operations.create_new_task(self.cursor, tsk)
        self.connection.commit()
        self.cursor.execute('SELECT * FROM tasks WHERE title = ?', (tsk.title,))
        row = self.cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[1], tsk.title)
        self.assertEqual(row[2], tsk.priority)
        self.assertEqual(row[3], tsk.content)
        self.assertEqual(row[6], tsk.is_done)

    def test_update_priority_on_undone_task(self):
        tsk = self.insert_task()
        database_operations.update_priority(self.cursor, tsk.title, 2)
        self.connection.commit()
        self.cursor.execute('SELECT priority FROM tasks WHERE title = ?', (tsk.title,))
        priority = self.cursor.fetchone()[0]
        self.assertEqual(priority, 2)

    def test_update_priority_on_done_task_raises(self):
        tsk = self.insert_task()
        self.cursor.execute('UPDATE tasks SET is_done = TRUE WHERE title = ?', (tsk.title,))
        self.connection.commit()
        with self.assertRaises(ValueError):
            database_operations.update_priority(self.cursor, tsk.title, 2)

    def test_update_content_on_undone_task(self):
        tsk = self.insert_task()
        new_content = "Updated content for testing"
        database_operations.update_content(self.cursor, tsk.title, new_content)
        self.connection.commit()
        self.cursor.execute('SELECT content FROM tasks WHERE title = ?', (tsk.title,))
        content = self.cursor.fetchone()[0]
        self.assertEqual(content, new_content)

    def test_update_content_on_done_task_raises(self):
        tsk = self.insert_task()
        self.cursor.execute('UPDATE tasks SET is_done = TRUE WHERE title = ?', (tsk.title,))
        self.connection.commit()
        with self.assertRaises(ValueError):
            database_operations.update_content(self.cursor, tsk.title, "Another content")

    def test_mark_as_done(self):
        tsk = self.insert_task()
        database_operations.mark_as_done(self.cursor, tsk.title)
        self.connection.commit()
        self.cursor.execute('SELECT is_done FROM tasks WHERE title = ?', (tsk.title,))
        is_done = self.cursor.fetchone()[0]
        self.assertTrue(is_done)

    def test_mark_as_done_already_done_raises(self):
        tsk = self.insert_task()
        self.cursor.execute('UPDATE tasks SET is_done = TRUE WHERE title = ?', (tsk.title,))
        self.connection.commit()
        with self.assertRaises(ValueError):
            database_operations.mark_as_done(self.cursor, tsk.title)

    def test_remove_task(self):
        tsk = self.insert_task()
        database_operations.remove_task(self.cursor, tsk.title)
        self.connection.commit()
        self.cursor.execute('SELECT * FROM tasks WHERE title = ?', (tsk.title,))
        self.assertIsNone(self.cursor.fetchone())

    def test_get_list_of_tasks_returns_correct_tasks(self):
        t1 = self.make_task(title="Title1", is_done=False)
        t2 = self.make_task(title="Title2", is_done=True)
        t3 = self.make_task(title="Title3", is_done=False)
        for t in [t1, t2, t3]:
            self.insert_task(t)
        tasks = database_operations.get_list_of_tasks(self.cursor)
        titles = [tsk.title for tsk in tasks]
        self.assertIn("Title1", titles)
        self.assertIn("Title2", titles)
        self.assertIn("Title3", titles)
        undone_tasks = database_operations.get_list_of_tasks(self.cursor, only_undone=True)
        undone_titles = [tsk.title for tsk in undone_tasks]
        self.assertIn("Title1", undone_titles)
        self.assertIn("Title3", undone_titles)
        self.assertNotIn("Title2", undone_titles)


if __name__ == "__main__":
    unittest.main()
