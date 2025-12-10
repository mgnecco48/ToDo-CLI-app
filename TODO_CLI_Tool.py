import os
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.shortcuts import (
    radiolist_dialog,
    input_dialog,
    yes_no_dialog)
from prompt_toolkit.application.current import get_app_session
from prompt_toolkit.styles import Style


matrix_style = Style.from_dict({
    "dialog": "bg:#000000 #00ff00",
    "dialog frame.label": "bg:#000000 #00ff00",
    "dialog.body": "bg:#000000 #00ff00",
    "dialog shadow": "bg:#003300",
})

solarized_dark = Style.from_dict({
    "dialog": "bg:#002b36 #93a1a1",
    "dialog frame.label": "bg:#073642 #b58900",
    "dialog.body": "bg:#002b36 #839496",
    "dialog shadow": "bg:#001f27",
})

sunset = Style.from_dict({
    "dialog": "bg:#2b1b17 #ffd8b5",
    "dialog frame.label": "bg:#402319 #ff8c42",
    "dialog.body": "bg:#2b1b17 #ffd8b5",
    "dialog shadow": "bg:#1a0f0b",
})

pastel_breeze = Style.from_dict({
    "dialog": "bg:#f2faff #4a4a4a",
    "dialog frame.label": "bg:#dceeff #6aa6ff",
    "dialog.body": "bg:#f2faff #4a4a4a",
    "dialog shadow": "bg:#c9ddea",
})

hacker = Style.from_dict({
    "dialog": "bg:#000000 #33ff33",
    "dialog frame.label": "bg:#003300 #66ff66",
    "dialog.body": "bg:#000000 #33ff33",
    "dialog shadow": "bg:#001a00",
})

terminal_amber = Style.from_dict({
    "dialog": "bg:#000000 #ffbf00",
    "dialog frame.label": "bg:#1a0f00 #ffcc33",
    "dialog.body": "bg:#000000 #ffbf00",
    "dialog shadow": "bg:#260f00",
})

# To change the theme for all dialogs:
dialog_style = matrix_style


def load_tasks(filepath):
    """Load tasks from file in human-readable format."""
    tasks = []
    if not os.path.exists(filepath):
        return tasks

    with open(filepath, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue

            if line.startswith("✔ "):
                text = line[2:].strip()
                done = True
            elif line.startswith("✖ "):
                text = line[2:].strip()
                done = False
            else:
                # Old format: plain line = not done
                text = line
                done = False

            tasks.append({"text": text, "done": done})

    return tasks


def save_tasks(filepath, tasks):
    """Save tasks to file in human-readable format."""
    with open(filepath, "w") as f:
        for task in tasks:
            icon = "✔" if task["done"] else "✖"
            f.write(f"{icon} {task['text']}\n")


def format_task(task):
    icon = "✔" if task["done"] else "✖"
    color = "ansigreen" if task["done"] else "ansired"
    return f"<{color}>{icon}</{color}> {task['text']}"


def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TASK_FILE = os.path.join(BASE_DIR, "ToDo_Tasks.txt")

    tasks = load_tasks(TASK_FILE)

    while True:
        # Build task list text for the dialog
        if not tasks:
            task_list_text = "No tasks yet."
        else:
            task_list_text = "\n".join(
                f"{i}. {format_task(task)}"
                for i, task in enumerate(tasks, 1)
            )
        # Creating the correct size separator line:
        # It wont resize dinamically
        session = get_app_session()
        width = session.output.get_size().columns
        line = "─" * (width - 5)

        choice = radiolist_dialog(
            title="TO DO List",
            text=HTML(
                f"Your tasks:\n\n"
                f"{task_list_text}\n\n"
                f"{line}\n\n"
                f"Choose an option:"
            ),
            values=[
                ("add", "Add task"),
                ("toggle", "Mark task as done/undone"),
                ("remove", "Remove task"),
                ("clear", "Clear all tasks"),
                ("quit", "Save + Quit"),
            ],
            style=dialog_style,
        ).run()

        if choice is None:
            continue

        # ADD
        if choice == "add":
            new_text = input_dialog(
                title="Add Task",
                text="Enter the new task:",
                style=dialog_style,
            ).run()

            if new_text:
                tasks.append(
                    {"text": new_text.strip().capitalize(), "done": False})
                print_formatted_text(HTML(
                    f'<ansigreen>"{new_text}" added.</ansigreen>'
                ))

        # TOGGLE DONE / NOT DONE
        elif choice == "toggle":
            if not tasks:
                print_formatted_text(
                    HTML("<ansired>No tasks to update.</ansired>"))
                continue

            values = [(str(i), task["text"])
                      for i, task in enumerate(tasks, 1)]

            toggle_choice = radiolist_dialog(
                title="Toggle Task",
                text="Select a task to mark as done/undone:",
                values=values,
                style=dialog_style,
            ).run()

            if toggle_choice:
                idx = int(toggle_choice) - 1
                tasks[idx]["done"] = not tasks[idx]["done"]
                state = "Done" if tasks[idx]["done"] else "Not done"
                print_formatted_text(HTML(
                    f'<ansigreen>Task marked as: {state}</ansigreen>'
                ))

        # REMOVE
        elif choice == "remove":
            if not tasks:
                print_formatted_text(
                    HTML("<ansired>No tasks to remove.</ansired>"))
                continue

            values = [(str(i), task["text"])
                      for i, task in enumerate(tasks, 1)]

            remove_choice = radiolist_dialog(
                title="Remove Task",
                text="Select a task:",
                values=values,
                style=dialog_style,
            ).run()

            if remove_choice:
                idx = int(remove_choice) - 1
                removed = tasks.pop(idx)
                print_formatted_text(HTML(
                    f'<ansired>Removed "{removed["text"]}".</ansired>'
                ))

        # CLEAR ALL
        elif choice == "clear":
            confirm = yes_no_dialog(
                title="Confirm",
                text="Delete ALL tasks?",
                style=dialog_style,
            ).run()

            if confirm:
                tasks = []
                print_formatted_text(
                    HTML("<ansired>All tasks cleared.</ansired>"))

        # SAVE + QUIT
        elif choice == "quit":
            save_tasks(TASK_FILE, tasks)
            print_formatted_text(HTML("<ansigreen>Goodbye!</ansigreen>"))
            break


if __name__ == "__main__":
    main()
