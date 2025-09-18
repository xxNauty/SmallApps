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
            raise TypeError(f"Title of the task should be of string type, found {type(title)}")
        elif len(title) < 3:
            raise ValueError("Title of the task should be at least 3 characters long")
        elif len(title) > 25:
            raise ValueError("Title of the task cannot be longer than 25 characters")
        else:
            self.title = title

        if not isinstance(priority, int):
            raise TypeError(f"Priority of the task should be of integer type, found {type(priority)}")
        elif not(1 <= priority <= 3):
            raise ValueError("The value of the priority should be in range from 1 to 3, both inclusive")
        else:
            self.priority = priority

        if not isinstance(content, str):
            raise TypeError(f"Content of the task should be of string type, found {type(content)}")
        elif len(content) < 10:
            raise ValueError("Content of the task should be at least 10 character long")
        else:
            self.content = content

        if not isinstance(due_to, datetime):
            raise TypeError(f"Due to date should be of datetime type, found {type(due_to)}")
        elif due_to <= created_at:
            raise ValueError("Due to date must be after created at date")
        else:
            self.due_to = due_to

        if not isinstance(created_at, datetime):
            raise TypeError(f"Created at date should be of datetime type, found {type(created_at)}")
        else:
            self.created_at = created_at

        if not isinstance(is_done, bool):
            raise TypeError(f"Is done should be of type boolean, found {type(is_done)}")
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

    @staticmethod
    def from_tuple(data: tuple[int, str, int, str, str, str, int]) -> "Task": # cudzysłowia wymagane są podczas odwoływania się do klasy wewnątrz niej samej
        return Task(
            data[1],
            data[2],
            data[3],
            datetime.strptime(data[4], "%Y-%m-%d %H:%M:%S"),
            datetime.strptime(data[5], "%Y-%m-%d %H:%M:%S.%f"),
            True if data[6] == 1 else False
        )
