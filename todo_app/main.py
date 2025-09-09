import datetime
import sqlite3

import database.database_operations as db
from task import Task


def main() -> None:
    close_app = False
    print("---TODO App---\n")
    while not close_app:
        print(
            "1. Add new task\n"
            "2. Update priority of existing task\n"
            "3. Update content of existing task\n"
            "4. Mark task as done\n"
            "5. Remove task\n"
            "6. Get list of tasks\n"
            "7. Close app"
        )
        action = int(input("Choose what you want to do: "))
        print("\n")

        match action:
            case 1:
                title = input("Choose title for your task: ")
                priority = int(input("How high is the priority? (1 -> lowest, 3 -> highest): "))
                content = input("Explain this task: ")
                due_to = input("When it should be finished? (format: YYYY-mm-dd HH:MM:SS):")

                due_to_datetime = datetime.datetime.strptime(due_to,"%Y-%m-%d %H:%M:%S")
                try:
                    task = Task(
                        title,
                        priority,
                        content,
                        due_to_datetime
                    )
                    db.create_new_task(task)
                except (TypeError, ValueError) as error:
                    print(error)
                except sqlite3.Error as error:
                    print("Other type of error:", error)
                else:
                    print("\nTask created successfully\nWhat do you want to do now?")

            case 2:
                title = input("Pass title of the task you want to change priority of: ")
                new_priority = int(input("Set new priority (1 -> lowest, 3 -> highest):"))

                try:
                    db.update_priority(title, new_priority)
                except sqlite3.Error as error:
                    print("Other type of error:", error)
                else:
                    print("New priority set\n")
            case 3:
                title = input("Pass title of the task you want to change content: ")
                new_content = input("Write new content of this task: ")

                try:
                    db.update_content(title, new_content)
                except sqlite3.Error as error:
                    print("Other type of error:", error)
                else:
                    print("New content set\n")
            case 4:
                title = input("Choose which task to mark as done: ")

                try:
                    db.mark_as_done(title)
                except sqlite3.Error as error:
                    print("Other type of error:", error)
                else:
                    print("Task marked as done\n")
            case 5:
                title = input("Choose which task you want to remove: ")

                try:
                    db.remove_task(title)
                except sqlite3.Error as error:
                    print("Other type of error:", error)
                else:
                    print("Task removed successfully\n")
            case 6:
                only_undone = input("Do you want to see only undone tasks? (Y/N)")
                only_undone = True if only_undone.upper() == "Y" else False
                try:
                    tasks = db.get_list_of_tasks(only_undone)
                except sqlite3.Error as error:
                    print("Other type of error:", error)
                else:
                    print("--------------------------------")
                    if tasks:
                        print("\n")
                        for task in tasks:
                            print(task)
                        print("\n")
                    else:
                        print("There is no tasks in the database\n")
                    print("--------------------------------")

            case 7:
                close_app = True
            case _:
                print("Wrong action!\n")

if __name__ == "__main__":
    main()
