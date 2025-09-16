from task import Task
from datetime import datetime
from sqlite3 import Error as sqlite_error
from database import database_operations

def main() -> None:
    cursor = database_operations.init_database()
    print("---TODO App---\n")
    while True:
        print(
            "1. Add new task\n"
            "2. Update priority of existing task\n"
            "3. Update content of existing task\n"
            "4. Mark task as done\n"
            "5. Remove task\n"
            "6. Get list of tasks\n"
            "7. Close app"
        )
        action = input("Choose what you want to do: ")
        try:
            action = int(action)
        except ValueError:
            print("You should write number of action you want to choose")
            continue
        else:
            match action:
                case 1:
                    while True:
                        title = input("Choose title for your task: ")

                        priority = input("How high is the priority? (1 -> lowest, 3 -> highest): ")
                        try:
                            priority = int(priority)
                        except ValueError:
                            print("Priority value should be of type integer")
                            continue

                        content = input("Explain this task: ")

                        due_to = input("When it should be finished? (format: YYYY-mm-dd HH:MM:SS):")
                        try:
                            due_to = datetime.strptime(due_to,"%Y-%m-%d %H:%M:%S")
                        except ValueError:
                            print("Given date is not in supported format")
                            continue

                        try:
                            task = Task(
                                title,
                                priority,
                                content,
                                due_to
                            )
                            database_operations.create_new_task(cursor, task)
                        except (TypeError, ValueError) as error:
                            print(error)
                            continue
                        except sqlite_error as error:
                            print("Other type of error:", error)
                            continue
                        else:
                            print("\nTask created successfully\nWhat do you want to do now?")
                            break

                case 2:
                    title = input("Pass title of the task you want to change priority of: ")
                    new_priority = int(input("Set new priority (1 -> lowest, 3 -> highest):"))

                    try:
                        database_operations.update_priority(cursor, title, new_priority)
                    except sqlite_error as error:
                        print("Other type of error:", error)
                    except PermissionError as error:
                        print(error)
                    else:
                        print("New priority set\n")
                case 3:
                    title = input("Pass title of the task you want to change content: ")
                    new_content = input("Write new content of this task: ")

                    try:
                        database_operations.update_content(cursor, title, new_content)
                    except sqlite_error as error:
                        print("Database error:", error)
                    except PermissionError as error:
                        print(error)
                    else:
                        print("New content set\n")
                case 4:
                    title = input("Choose which task to mark as done: ")

                    try:
                        database_operations.mark_as_done(cursor, title)
                    except sqlite_error as error:
                        print("Other type of error:", error)
                    except PermissionError as error:
                        print(error)
                    else:
                        print("Task marked as done\n")
                case 5:
                    title = input("Choose which task you want to remove: ")

                    try:
                        database_operations.remove_task(cursor, title)
                    except sqlite_error as error:
                        print("Other type of error:", error)
                    else:
                        print("Task removed successfully\n")
                case 6:
                    only_undone = input("Do you want to see only undone tasks? (Y/N)")
                    only_undone = True if only_undone.upper() == "Y" else False
                    try:
                        tasks = database_operations.get_list_of_tasks(cursor, only_undone)
                    except sqlite_error as error:
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
                    break
                case _:
                    print("There is no such option\n")

if __name__ == "__main__":
    main()
