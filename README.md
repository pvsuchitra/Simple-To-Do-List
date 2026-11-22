# A Simple-ToDo-List

### This is a simple To-Do List web app built using Flask and CSV for storage.

🌟 Features
<p>1️⃣ View Tasks → Displays a list of tasks from a CSV file.</p>
<p>2️⃣ Add Tasks → Users can add new tasks, which are saved in TaskList.csv.</p>
<p>3️⃣ Mark Tasks as Completed → Clicking "Complete" updates the task's status to "Completed".</p>
<p>4️⃣ Delete Tasks → Clicking "Delete" removes the task from the list.</p>

🔧 Tech Stack
<p>Backend: Flask (Python)</p>
<p>Storage: CSV file (TaskList.csv)</p>
<p>Frontend: HTML + Jinja2 for templates</p>

# Simple To-Do List

A lightweight, database-free To-Do List web application built with **Flask**, **Jinja2**, and **CSV** flat-file storage.

## Features
- **View Tasks:** Reads and displays all saved tasks from `TaskList.csv`.
- **Add Tasks:** Appends new tasks directly to `TaskList.csv`.
- **Mark as Completed:** Updates a task's status to `Completed`.
- **Delete Tasks:** Removes tasks from the list and updates the CSV file.

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML, Jinja2
- **Storage:** Local CSV (`TaskList.csv`)

## Project Structure
```text
Simple-To-Do-List/
├── templates/          # HTML templates (Jinja2)
├── Simple-ToDo.py      # Main Flask application and routes
├── TaskList.csv        # Flat-file task storage
├── requirements.txt    # Python dependencies
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8+
- `pip`

### Installation & Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/pvsuchitra/Simple-To-Do-List.git](https://github.com/pvsuchitra/Simple-To-Do-List.git)
   cd Simple-To-Do-List
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python Simple-ToDo.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Notes
- Because tasks are stored in a local CSV file (`TaskList.csv`), this application is intended for single-user local use rather than concurrent multi-user production deployments.
