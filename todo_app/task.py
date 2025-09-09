from datetime import datetime

class Task:
    def __init__(
            self,
            title: str,
            priority: int,
            content: str,
            due_to: datetime,
            created_at: datetime = datetime.now(),
            is_done: bool = False
    ):
        if not isinstance(title, str):
            raise TypeError("Title of the task should be of string type")
        elif len(title) < 3:
            raise ValueError("Title of the task should be at least 3 characters long")
        elif len(title) > 25:
            raise ValueError("Title of the task cannot be longer than 25 characters")
        else:
            self.title = title

        if not isinstance(priority, int):
            raise TypeError("Priority of the task should be of integer type")
        elif not(1 <= priority <= 3):
            raise ValueError("The value of the priority should be in range from 1 to 3, both inclusive")
        else:
            self.priority = priority

        if not isinstance(content, str):
            raise TypeError("Content of the task should be of string type")
        elif len(content) < 10:
            raise ValueError("Content of the task should be at least 10 character long")
        else:
            self.content = content

        if not isinstance(due_to, datetime):
            raise TypeError("Due to date should be of datetime type")
        elif due_to <= created_at:
            raise ValueError("Due to date must be after created at date")
        else:
            self.due_to = due_to

        if not isinstance(created_at, datetime):
            raise TypeError("Created at date should be of datetime type")
        else:
            self.created_at = created_at

        if not isinstance(is_done, bool):
            raise TypeError("Is done should be of type boolean")
        else:
            self.is_done = is_done

    def __str__(self) -> str:
        datetime_due_to = datetime.strptime(str(self.due_to), "%Y-%m-%d %H:%M:%S")
        datetime_created_at = datetime.strptime(str(self.created_at), "%Y-%m-%d %H:%M:%S.%f")
        return (
            f"{{\n\tTile: {self.title},"
            f"\n\tPriority: {self.priority},"
            f"\n\tContent: {self.content},"
            f"\n\tDue to: {datetime_due_to.strftime("%Y-%m-%d %H:%M:%S")},"
            f"\n\tCreated at: {datetime_created_at.strftime("%Y-%m-%d %H:%M:%S")},"
            f"\n\tIs done?: {"True" if self.is_done else "False"}\n}}"
        )

    def __repr__(self) -> str:
        return (f"Title: {self.title}, Priority: {self.priority}, Content: {self.content}, Due to: {self.due_to}, "
                f"Created at: {self.created_at}, Is done: {self.is_done}")
