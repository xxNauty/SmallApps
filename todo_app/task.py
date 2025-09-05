from datetime import datetime

class Task:
    def __init__(self, name: str, priority: int, content: str, due_to: datetime):
        self.name = name
        self.priority = priority
        self.content = content
        self.created_at = datetime.now()
        self.due_to = due_to
        self.is_done = False