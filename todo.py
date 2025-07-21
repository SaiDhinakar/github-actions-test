todos = {}

def add_todo(task):
    """Add a new todo item."""
    if task in todos:
        print(f"Todo '{task}' already exists.")
    else:
        todos[task] = False
        print(f"Todo '{task}' added.")

def complete_todo(task):
    """Mark a todo item as completed."""
    if task in todos:
        todos[task] = True
        print(f"Todo '{task}' marked as completed.")
    else:
        print(f"Todo '{task}' does not exist.")
        
