import json

from src.task_manager import TaskManager


def get_user_input(prompt: str) -> str:
    """
    Prompt the user for input and return the stripped string

    Parameters:
        prompt (str): The text displayed to the user to elicit input

    Returns:
        str: The user input without any leading/trailing whitespace
    """
    return input(prompt).strip()


def print_commands() -> None:
    """
    Print all the available commands and their usage.
    """
    commands = {
        "add task": "Add a new task",
        "add label": "Add a label to a task",
        "add subtask": "Add a subtask to a task",
        "delete": "Delete a task",
        "update": "Update a task",
        "restore": "Restore a deleted task",
        "get tasks": "Get all tasks",
        "get subtasks": "Get all subtasks for a task",
        "exit": "Exit the program"
    }
    print("Available commands:")
    for command, description in commands.items():
        print(f"  {command}: {description}")


def handle_task_update(task_manager: TaskManager) -> dict[str, any]:
    """
    Update the details of an existing task based on user input

    Parameters:
        task_manager TaskManager: The task_manager instance managing the tasks

    Returns:
        dict[str, any]: The result of the task update operation
    """
    task_id = int(get_user_input("Enter task id: "))
    title = get_user_input("Enter title: ")
    description = get_user_input("Enter description: ")
    status = get_user_input("Enter status: ")
    due_date = get_user_input("Enter due date (YYYY-MM-DD): ")

    return task_manager.update_task(task_id, title, description, status, due_date)


def handle_add_task(task_manager: TaskManager) -> dict[str, any]:
    """
    Handle the addition of a new task based on user input

    Parameters:
        task_manager TaskManager: The task_manager instance managing the tasks

    Returns:
        dict[str, any]: The result of the task addition operation
    """
    title = get_user_input("Enter title: ")
    description = get_user_input("Enter description: ")
    due_date = get_user_input("Enter due date (YYYY-MM-DD): ")

    return task_manager.add_task(title, description, due_date)


def handle_add_label(task_manager: TaskManager) -> dict[str, any]:
    """
    Add a label to a specific task based on user input

    Parameters:
        task_manager (TaskManager): The task_manager instance managing the tasks

    Returns:
        dict[str, any]: The result of adding a label to a task
    """
    task_id = int(get_user_input("Enter task id: "))
    label_text = get_user_input("Enter label: ")

    return task_manager.add_label_to_task(task_id, label_text)


def handle_add_subtask(task_manager: TaskManager) -> dict[str, any]:
    """
    Add a subtask to a specific task based on user input

    Parameters:
        task_manager (TaskManager): The task_manager instance managing the tasks

    Returns:
        dict[str, any]: The result of the subtask addition operation
    """
    task_id = int(get_user_input("Enter task id: "))
    title = get_user_input("Enter title: ")
    description = get_user_input("Enter description: ")
    due_date = get_user_input("Enter due date (YYYY-MM-DD): ")

    return task_manager.add_subtask(task_id, title, description, due_date)


def handle_task_deletion(task_manager: TaskManager) -> dict[str, any]:
    """
    Delete a specific task based on user input

    Parameters:
        task_manager: (TaskManager): The task_manager instance managing the tasks

    Returns:
        dict[str, any]: The result of the task deletion operation
    """
    task_id = int(get_user_input("Enter task id: "))
    return task_manager.delete_task(task_id)


def handle_task_restore(task_manager: TaskManager) -> dict[str, any]:
    """
    Restore a previously deleted task based on user input

    Parameters:
        task_manager TaskManager: The task_manager instance managing the tasks

    Returns:
        dict[str, any]: The result of the task restoration operation
    """
    task_id = int(get_user_input("Enter task id: "))
    return task_manager.restore_task(task_id)


def handle_get_subtasks(task_manager: TaskManager) -> dict[str, any]:
    """
    Retrieve subtasks for a specific task based on user input

    Parameters:
        task_manager TaskManager: The task_manager instance managing the tasks

    Returns:
        dict[str, any]: The list of subtasks associated with the given task
    """
    task_id = int(get_user_input("Enter task id: "))
    return task_manager.get_subtasks(task_id)


def main() -> None:
    """
    Main function to handle user inputs and delegate task operations.
    Continuously prompts the user for commands and executes corresponding actions.
    """
    user_id = int(get_user_input("What is your user id? "))
    task_manager = TaskManager(user_id)

    while True:
        user_input = get_user_input("Command (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting program.")
            break

        args = user_input.split()
        command = args[0].lower()
        sub_command = args[1].lower() if len(args) > 1 else None

        task_result = None
        if command == "add":
            if sub_command == "task":
                task_result = handle_add_task(task_manager)
            elif sub_command == "label":
                task_result = handle_add_label(task_manager)
            elif sub_command == "subtask":
                task_result = handle_add_subtask(task_manager)
        elif command == "delete":
            task_result = handle_task_deletion(task_manager)
        elif command == "update":
            task_result = handle_task_update(task_manager)
        elif command == "restore":
            task_result = handle_task_restore(task_manager)
        elif command == "get":
            if sub_command == "tasks":
                task_result = task_manager.get_tasks()
            elif sub_command == "subtasks":
                task_result = handle_get_subtasks(task_manager)

        if task_result is None:
            print("Unknown command")
            print_commands()
            continue

        print(json.dumps(task_result, indent=4))


if __name__ == "__main__":
    main()
