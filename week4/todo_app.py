import json

# Handles reading/writing JSON file
class JsonHandler:
    def __init__(self, filename="todos.json"):
        self.filename = filename

    def read_json(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            # If file doesn't exist, start with empty list
            return []

    def write_json(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)


# Handles task operations (Add, View, Update, Delete)
class TodoManager:
    def __init__(self):
        self.storage = JsonHandler()
        self.tasks = self.storage.read_json()
        self.next_id = len(self.tasks) + 1

    def add(self, title):
        task = {"id": self.next_id, "title": title, "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        self.storage.write_json(self.tasks)
        print("Added:", task)

    def view(self):
        if not self.tasks:
            print("No tasks yet.")
        for t in self.tasks:
            status = "Yes" if t["completed"] else "No"
            print(f"ID: {t['id']} | Title: {t['title']} | Completed: {status}")

    def update(self, task_id, new_title=None, completed=None):
        for t in self.tasks:
            if t["id"] == task_id:
                if new_title:
                    t["title"] = new_title
                if completed is not None:
                    t["completed"] = completed
                self.storage.write_json(self.tasks)
                print("Updated:", t)
                return
        print("Task not found.")

    def delete(self, task_id):
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        if len(self.tasks) < before:
            self.storage.write_json(self.tasks)
            print("Deleted task", task_id)
        else:
            print("Task not found.")


# CLI loop
def main():
    manager = TodoManager()
    while True:
        print("\n1. Add | 2. View | 3. Update | 4. Delete | 5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            title = input("Title: ")
            manager.add(title)
        elif choice == "2":
            manager.view()
        elif choice == "3":
            task_id = int(input("Task ID: "))
            new_title = input("New title (blank to skip): ")
            status = input("Completed? (y/n/blank): ").lower()
            completed = None
            if status == "y":
                completed = True
            elif status == "n":
                completed = False
            manager.update(task_id, new_title or None, completed)
        elif choice == "4":
            task_id = int(input("Task ID: "))
            manager.delete(task_id)
        elif choice == "5":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
