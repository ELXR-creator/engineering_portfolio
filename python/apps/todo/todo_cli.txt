todos = {}
counter = 1

print("👋 Welcome to CLI Todo App")

def add_task(todos, counter):
    task = input("Enter task: ").strip()
    if not task:
        print("❌ Task cannot be empty")
        return counter

    todos[counter] = task
    print(f"✅ Task added at #{counter}")
    return counter + 1


def show_tasks(todos):
    if not todos:
        print("📭 No tasks found")
        return

    print("\n📋 Your Tasks:")
    for key, task in todos.items():
        print(f"{key}. {task}")
    print()


def remove_task(todos):
    show_tasks(todos)
    try:
        idx = int(input("Enter task number to remove: "))
        if idx in todos:
            del todos[idx]
            print("🗑️ Task removed")
        else:
            print("❌ Task not found")
    except ValueError:
        print("❌ Please enter a valid number")


def update_task(todos):
    show_tasks(todos)
    try:
        idx = int(input("Enter task number to update: "))
        if idx in todos:
            new_task = input("Enter new task: ").strip()
            if not new_task:
                print("❌ Task cannot be empty")
                return
            todos[idx] = new_task
            print("✏️ Task updated")
        else:
            print("❌ Task not found")
    except ValueError:
        print("❌ Please enter a valid number")


while True:
    command = input("Command (add / show / rm / update / exit): ").strip().lower()

    match command:
        case "add":
            counter = add_task(todos, counter)
        case "show":
            show_tasks(todos)
        case "rm":
            remove_task(todos)
        case "update":
            update_task(todos)
        case "exit":
            print("👋 Goodbye!")
            break
        case _:
            print("❓ Unknown command")
