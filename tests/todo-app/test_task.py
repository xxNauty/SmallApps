import unittest

from datetime import datetime
from todo_app.task import Task

class TestTask(unittest.TestCase):

    def setUp(self):
        self.title = "Example Task"
        self.priority = 2
        self.content = "This is a valid content."
        self.created_at = datetime(2024, 6, 1, 12, 0, 0, 123456)
        self.due_to = datetime(2025, 1, 1, 20, 0, 0)
        self.is_done = True

    def test_valid_task_creation(self):
        task = Task(
            self.title,
            self.priority,
            self.content,
            self.due_to,
            self.created_at,
            self.is_done
        )
        self.assertEqual(task.title, self.title)
        self.assertEqual(task.priority, self.priority)
        self.assertEqual(task.content, self.content)
        self.assertEqual(task.due_to, self.due_to)
        self.assertEqual(task.created_at, self.created_at)
        self.assertEqual(task.is_done, self.is_done)

    def test_title_type(self):
        with self.assertRaises(TypeError):
            Task(123, self.priority, self.content, self.due_to, self.created_at)

    def test_title_too_short(self):
        with self.assertRaises(ValueError):
            Task("ab", self.priority, self.content, self.due_to, self.created_at)

    def test_title_too_long(self):
        with self.assertRaises(ValueError):
            Task("a" * 26, self.priority, self.content, self.due_to, self.created_at)

    def test_priority_type(self):
        with self.assertRaises(TypeError):
            Task(self.title, "high", self.content, self.due_to, self.created_at)

    def test_priority_out_of_range_low(self):
        with self.assertRaises(ValueError):
            Task(self.title, 0, self.content, self.due_to, self.created_at)

    def test_priority_out_of_range_high(self):
        with self.assertRaises(ValueError):
            Task(self.title, 4, self.content, self.due_to, self.created_at)

    def test_content_type(self):
        with self.assertRaises(TypeError):
            Task(self.title, self.priority, 12345, self.due_to, self.created_at)

    def test_content_too_short(self):
        with self.assertRaises(ValueError):
            Task(self.title, self.priority, "short", self.due_to, self.created_at)

    def test_due_to_type(self):
        with self.assertRaises(TypeError):
            Task(self.title, self.priority, self.content, "2024-06-02", self.created_at)

    def test_due_to_the_same_as_created_at(self):
        with self.assertRaises(ValueError):
            Task(self.title, self.priority, self.content, self.created_at, self.created_at)

    def test_created_at_type(self):
        with self.assertRaises(TypeError):
            Task(self.title, self.priority, self.content, self.due_to, "2024-06-01")

    def test_is_done_type(self):
        with self.assertRaises(TypeError):
            Task(self.title, self.priority, self.content, self.due_to, self.created_at, "yes")

    def test_str_method(self):
        task = Task(self.title, self.priority, self.content, self.due_to, self.created_at, True)
        result = str(task)
        self.assertIn("Tile: Example Task", result)
        self.assertIn("Priority: 2", result)
        self.assertIn("Content: This is a valid content.", result)
        self.assertIn("Is done?: True", result)

    def test_repr_method(self):
        task = Task(self.title, self.priority, self.content, self.due_to, self.created_at, False)
        result = repr(task)
        self.assertIn(f"Title: {self.title}", result)
        self.assertIn(f"Priority: {self.priority}", result)
        self.assertIn(f"Content: {self.content}", result)
        self.assertIn("Is done: False", result)

if __name__ == "__main__":
    unittest.main()