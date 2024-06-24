class Task:
    def __init__(self, title, description="", due_date=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}"

    def mark_as_completed(self):
        self.completed = True

    def update(self, title=None, description=None, due_date=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, index, title=None, description=None, due_date=None):
        if 0 <= index < len(self.tasks):
            self.tasks[index].update(title, description, due_date)
        else:
            print("Invalid task index")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index")

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"\nTask {i + 1}:\n{task}\n")

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Invalid task index")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Display Tasks")
        print("5. Mark Task as Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date: ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == '2':
            index = int(input("Enter task index to update: ")) - 1
            title = input("Enter new task title (leave blank to keep current): ")
            description = input("Enter new task description (leave blank to keep current): ")
            due_date = input("Enter new task due date (leave blank to keep current): ")
            todo_list.update_task(index, title, description, due_date)
            print("Task updated successfully!")

        elif choice == '3':
            index = int(input("Enter task index to delete: ")) - 1
            todo_list.delete_task(index)
            print("Task deleted successfully!")

        elif choice == '4':
            todo_list.display_tasks()

        elif choice == '5':
            index = int(input("Enter task index to mark as completed: ")) - 1
            todo_list.mark_task_as_completed(index)
            print("Task marked as completed!")

        elif choice == '6':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
