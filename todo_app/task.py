from datetime import datetime

class Task:
    def __init__(
            self,
            name: str,
            priority: int,
            content: str,
            due_to: datetime,
            created_at: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            is_done: bool = False
    ):
        self.name = name
        self.priority = priority
        self.content = content
        self.due_to = due_to
        self.created_at = created_at
        self.is_done = is_done

    def __str__(self) -> str:
        datetime_due_to = datetime.strptime(str(self.due_to), "%Y-%m-%d %H:%M:%S")
        datetime_created_at = datetime.strptime(str(self.created_at), "%Y-%m-%d %H:%M:%S")
        return (
            f"{{\n\tTile: {self.name},"
            f"\n\tPriority: {self.priority},"
            f"\n\tContent: {self.content},"
            f"\n\tDue to: {datetime_due_to.strftime("%d.%m.%Y %H:%M:%S")},"
            f"\n\tCreated at: {datetime_created_at.strftime("%d.%m.%Y %H:%M:%S")},"
            f"\n\tIs done?: {"True" if self.is_done else "False"}\n}}"
        )

    def __repr__(self) -> str:
        return (f"Title: {self.name}, Priority: {self.priority}, Content: {self.content}, Due to: {self.due_to}, "
                f"Created at: {self.created_at}, Is done: {self.is_done}")
