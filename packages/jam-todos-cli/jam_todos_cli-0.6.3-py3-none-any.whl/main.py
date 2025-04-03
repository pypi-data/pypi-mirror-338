#type: ignore
import typer
from rich.console import Console
from rich.table import Table
import json
import os

app = typer.Typer()
console = Console()
TODO_FILE = "todos.json"

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=4)
        
@app.command()
def add(task: str):
    """Add a new task to the todo list."""
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    console.print(f"[green]Added task:[/green] {task}")
    
@app.command()
def list():
    """List all tasks in the todo list."""
    todos = load_todos()
    if not todos:
        console.print("[yellow]No tasks yet! Add some.[/yellow]")
        return
    table = Table(title="Todo List", show_header=True, header_style="bold magenta", title_style="bold magenta")
    table.add_column("ID", style="cyan")
    table.add_column("Task", style="magenta")
    table.add_column("Done?", style="green")
    
    for i, todo in enumerate(todos, start=1):
        done = "✅" if todo["done"] else "❌"
        table.add_row(str(i), todo["task"], done)
    
    console.print(table)

@app.command()
def complete(task_id: int):
    """Mark a task as done."""
    tasks = load_todos()
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]["done"] = True
        save_todos(tasks)
        console.print(f"[green]Completed task:[/green] {tasks[task_id - 1]['task']}")
    else:
        console.print("[red]Invalid task ID![/red]")

@app.command()
def delete(task_id: int):
    """Delete a task."""
    tasks = load_todos()
    if 1 <= task_id <= len(tasks):
        deleted_task = tasks.pop(task_id - 1)
        save_todos(tasks)
        console.print(f"[green]Deleted task:[/green] {deleted_task['task']}")
    else:
        console.print("[red]Invalid task ID![/red]")

if __name__ == "__main__":
    app()

   
