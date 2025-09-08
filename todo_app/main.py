import datetime

import database.database_operations as db
from task import Task

def main() -> None:
    close_app = False

    while not close_app:
        print("TODO App\n\t"
              "1. Add new task\n\t"
              "2. Update priority of existing task\n\t"
              "3. Update content of existing task\n\t"
              "4. Mark task as done\n\t"
              "5. Remove task\n\t"
              "6. Get list of tasks\n\t"
              "7. Close app")
        action = int(input("Choose what you want to do: "))

        match action:
            case 1:
                title = input("Choose title for your task: ")
                priority = int(input("How high is the priority? (1 -> lowest, 3 -> highest): "))
                content = input("Explain this task: ")
                due_to = input("When it should be finished? (format: dd-mm-YYYY HH:MM:SS):")

                task = Task(
                    title,
                    priority,
                    content,
                    datetime.datetime.strptime(due_to, "%d-%m-%Y %H:%M:%S")
                )

                db.create_new_task(task)
                print("Task created successfully")
            case 2:
                title = input("Pass title of the task you want to change priority of: ")
                new_priority = int(input("Set new priority (1 -> lowest, 3 -> highest):"))

                db.update_priority(title, new_priority)
                print("New priority set")
            case 3:
                title = input("Pass title of the task you want to change content: ")
                new_content = input("Write new content of this task: ")

                db.update_content(title, new_content)
                print("New content set")
            case 4:
                title = input("Choose which task to mark as done: ")

                db.mark_as_done(title)
                print("Task marked as done")
            case 5:
                title = input("Choose which task you want to remove: ")

                db.remove_task(title)
                print("Task removed successfully")
            case 6:
                only_undone = input("Do you want to see only undone tasks? (Y/N)")
                only_undone = True if only_undone.upper() == "Y" else False
                tasks =  db.get_list_of_tasks(only_undone)
                if tasks:
                    for task in tasks:
                        print(task)
                else:
                    print("There is no tasks in the database")
            case 7:
                close_app = True
            case _:
                print("Wrong action!")

if __name__ == "__main__":
    main()
