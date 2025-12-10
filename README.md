# 📝 TODO CLI Tool  
A clean, interactive command-line TODO manager built in Python using **prompt_toolkit**.

This project demonstrates how to build a modern CLI application with dialogs, color themes, keyboard navigation, persistent storage, and a polished user experience.

---

## ✨ Features

- ✔ Interactive menu using radiolist dialogs  
- ✔ Add new tasks  
- ✔ Mark tasks as **done** / **not done**  
- ✔ Remove tasks  
- ✔ Clear all tasks with confirmation  
- ✔ Persistent storage in a local `.txt` file  
- ✔ Colored icons:  
  - **✔ Done** (green or theme color)  
  - **✖ Pending** (red or theme color)  
- ✔ Customizable themes (Matrix, Amber CRT, Dracula, Solarized, etc.)  
- ✔ Clean separation of logic: loading, saving, formatting, UI

---

## 📦 Installation

Make sure you have **Python 3.8+** installed.

Install dependencies:

```bash
pip install prompt_toolkit
```

Clone this repository:

```bash
git clone https://github.com/mgnecco48/ToDo-CLI-app.git
```

---

## ▶️ Usage

Run the app:

```bash
python todo.py
```

Or create a shell alias (optional):

```bash
alias todo="python /path/to/todo.py"
```

Now you can launch it simply by typing:

```bash
todo
```

---

## 📁 File Structure

```
.
├── todo.py                 # Main program
├── ToDo_Martin.txt         # Task storage (auto-generated)
└── README.md               # This file
```

---

## 🧠 How It Works

### Task Storage  
Tasks are saved in a human-readable format:

```
✔ Buy milk
✖ Clean room
```

Each line is parsed into a Python dictionary:

```
{"text": "Buy milk", "done": True}
```

### UI  
The tool uses `prompt_toolkit` dialogs:

- `radiolist_dialog` for menus  
- `input_dialog` for adding tasks  
- `yes_no_dialog` for confirmations  

Themes are defined using:

```
Style.from_dict({...})
```

You can easily switch between themes like:

- Matrix Green  
- Terminal Amber  
- Dracula  
- Solarized  
- Ice Blue  
- Cyberpunk  

Just change all occurences (Except for the theme creation) of the current theme,
to the correct style name.

---

## 🎨 Themes

This project includes several **built-in color themes**, allowing you to customize how the dialogs look.  
Each theme controls:

- dialog background  
- text color  
- frame label color  
- shadow color  

### Available Built-In Themes

Your script already defines the following themes:

```
matrix_style
solarized_dark
sunset
pastel_breeze
hacker
terminal_amber```

### How to apply a theme
Inside the script, the active theme is determined by the line:

```
dialog_style = matrix_style```

To use a different theme, simply change the name:

```
dialog_style = terminal_amber```

or:

```
dialog_style = solarized_dark````

Every dialog (radiolist_dialog, input_dialog, yes_no_dialog, etc.) uses this dialog_style, so changing it here updates the entire application.
---

## 🛠 Future Improvements

Planned enhancements:

- Sorting tasks (done last or done first)
- Categories (Work, Personal, Study, etc.)
- Priorities (High/Medium/Low)
- Due dates with validation
- Full-screen TUI layout (side panels, status bar)
- Export to JSON / Markdown

---

## 🤝 Contributing

Pull requests are welcome!  
If you'd like to contribute:

1. Fork the repo  
2. Create a feature branch  
3. Submit a Pull Request  

---

## ⭐ Acknowledgements

Built using:

- **Python**
- **prompt_toolkit**
- Terminal theming experiments
- A lot of learning and iteration!

---

If you like this project, please ⭐ star the repository!
