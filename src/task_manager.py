import requests
from src import config


class TaskManager:
    def __init__(self, user: int) -> None:
        """Initialize TaskManager with the users ID and Flask URL."""
        self.flask_url = config.FLASK_URL
        self.user_id = user

    def add_task(self, title: str, description: str, due_date: str) -> dict[str, any]:
        """Add a new task for the user."""
        url = f"{config.FLASK_URL}/users/{self.user_id}/tasks/"
        data = {
            "title": title,
            "description": description,
            "due_date": due_date,
        }
        response = requests.post(url, json=data)
        return response.json()

    def update_task(
        self, task_id: int, title: str, description: str, status: str, due_date: str
    ) -> dict[str, any]:
        """Update an existing task for the user."""
        url = f"{config.FLASK_URL}/users/{self.user_id}/tasks/{task_id}"
        data = {
            "title": title,
            "description": description,
            "status": status,
            "due_date": due_date,
            "user_id": self.user_id,
        }
        response = requests.put(url, json=data)
        return response.json()

    def delete_task(self, task_id: int) -> dict[str, any]:
        """Delete a task for the user."""
        url = f"{self.flask_url}/users/{self.user_id}/tasks/{task_id}"
        response = requests.delete(url)
        return response.json()

    def get_tasks(self) -> dict[str, any]:
        """Retrieve all tasks for the user."""
        url = f"{self.flask_url}/users/{self.user_id}/tasks"
        response = requests.get(url)
        return response.json()

    def get_deleted_tasks(self) -> dict[str, any]:
        """Retrieve all deleted tasks for the user."""
        url = f"{self.flask_url}/users/{self.user_id}/tasks"
        response = requests.get(url)
        return response.json()

    def get_subtasks(self, task_id: int) -> dict[str, any]:
        """Retrieve all subtasks for a specific task."""
        url = f"{self.flask_url}/users/{self.user_id}/tasks/{task_id}/subtasks"
        response = requests.get(url)
        return response.json()

    def add_subtask(
        self, parent_task_id: int, title: str, description: str, due_date: str
    ) -> dict[str, any]:
        """Add a new subtask to a specific task."""
        data = {
            "title": title,
            "description": description,
            "due_date": due_date,
        }
        url = f"{self.flask_url}/users/{self.user_id}/tasks/{parent_task_id}/subtasks"
        response = requests.post(url, json=data)
        return response.json()

    def add_label_to_task(self, task_id: int, label: str) -> dict[str, any]:
        """Add a label to a specific task."""
        url = f"{self.flask_url}/users/{self.user_id}/tasks/{task_id}/labels"
        data = {"label": label}
        response = requests.post(url, json=data)
        return response.json()

    def restore_task(self, task_id: int) -> dict[str, any]:
        """Restore a deleted task for the user."""
        url = f"{self.flask_url}/users/{self.user_id}/tasks/{task_id}/restore"
        response = requests.post(url)
        return response.json()
