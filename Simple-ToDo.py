from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)
TASK_File = os.path.join(os.path.dirname(__file__), "TaskList.csv")

# Load the task list from the file
def load_tasks():
    tasks = []
    try:
        with open(TASK_File, "r") as file:
            reader = csv.reader(file)
            next(reader, None)
            tasks = list(reader)
    except FileNotFoundError:
        pass
    return tasks

# Save the task list to the file
def save_tasks(tasks):
    with open(TASK_File, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Task", "Status","Priority"])  # Write the header
        writer.writerows(tasks)

# Display the task list
@app.route('/')
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

# Add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get("task_name")
    task_priority = request.form.get("task_priority")
    if task_name:
        tasks = load_tasks()
        tasks.append([task_name, "Pending",task_priority])
        save_tasks(tasks)
    return redirect(url_for('index'))

# Mark Tasks as Completed
@app.route('/complete/<int:task_id>')
def completed_tasks(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id][1] = "Completed"
        save_tasks(tasks)
    return redirect(url_for('index'))

# Delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
        save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
