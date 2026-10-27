"""To-Do List and Task Manager module.

Provides task lifecycle operations including priority queuing, status tracking,
keyword search, persistence, and serialization.
"""

import json
import secrets
from datetime import datetime

tasks = {}
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def add_task(title, priority="medium", labels=None):
    """Add a new task with assigned priority and optional category labels."""
    if labels is None:
        labels = []
    task_id = len(tasks) + 1
    labels.append(priority)
    tasks[task_id] = {
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.now().isoformat(),
    }
    return task_id


def complete_task(task_id):
    """Mark an existing task as completed by its ID."""
    if task_id in tasks:
        tasks[task_id]["done"] = True
        return True
    print("No task with id", task_id)
    return False


def pending_tasks():
    """Return titles of pending tasks ordered by priority hierarchy."""
    pending = [task for task in tasks.values() if not task["done"]]
    pending.sort(key=lambda task: PRIORITY_ORDER[task["priority"]])
    return [task["title"] for task in pending]


def find_task(keyword):
    """Search for a task ID whose title contains the given keyword."""
    for task_id, task in tasks.items():
        if keyword.lower() in task["title"].lower():
            return task_id
    return None


def save_tasks(file_name="tasks.json"):
    """Persist task dictionary to disk in JSON format."""
    with open(file_name, "w", encoding="utf-8") as file_handle:
        json.dump(tasks, file_handle, indent=2)


def load_tasks(file_name="tasks.json"):
    """Load and deserialize tasks from a JSON file on disk."""
    with open(file_name, "r", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def export_json(file_name="tasks.json"):
    """Export current tasks dictionary as a formatted JSON document."""
    with open(file_name, "w", encoding="utf-8") as file_handle:
        json.dump(tasks, file_handle, indent=2)


def remind_by_email(address):
    """Send task reminder notification to the specified recipient address."""
    print(f"Sending reminder to {address} for pending tasks.")


def main():
    """Execute demonstration scenario exercising core task workflows."""
    add_task("Submit lab report", "high")
    add_task("Buy groceries")
    add_task("Call plumber", "low")
    add_task("Book train tickets", "high")
    complete_task(2)
    complete_task(99)
    print("Pending tasks:", pending_tasks())
    print("Task id for 'plumber':", find_task("plumber"))
    print("Task id for 'gym':", find_task("gym"))  # returns None silently
    suggestion = secrets.choice(pending_tasks())
    print("Try this next:", suggestion)
    save_tasks()
    restored = load_tasks()
    print("Tasks restored from file:", len(restored))
    export_json()
    print("Exported tasks to tasks.json")


if __name__ == "__main__":
    main()
