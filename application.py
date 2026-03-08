from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "database.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''CREATE TABLE IF NOT EXISTS messages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  message TEXT NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DB_PATH)
    messages = conn.execute("SELECT * FROM messages").fetchall()
    conn.close()
    return render_template('index.html', messages=messages)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    message = request.form.get('message')
    if name and message:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("INSERT INTO messages (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
