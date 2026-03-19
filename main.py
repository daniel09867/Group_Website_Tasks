from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_tasks():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name, quantity, time FROM tasks")
    tasks = cursor.fetchall()

    conn.close()

    return tasks

def init_db():
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        quantity TEXT,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()

@app.route("/")
def index():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)