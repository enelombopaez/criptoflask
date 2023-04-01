import sqlite3
from . import app
from flask import Flask, render_template

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route("/purchase")
def purchase():
    return render_template('purchase.html')

@app.route("/status")
def status():
    return render_template('status.html')
