import sqlite3
from . import app
from flask import Flask, render_template
from .forms import PurchaseForm
from config import COINS

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_id():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM crypto')
    post= cur.fetchall()
    conn.close()
    return post


@app.route("/")
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM crypto').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route("/purchase")
def purchase():
    form = PurchaseForm()
    coins = COINS
    return render_template('purchase.html', coins=coins, form=form)

@app.route("/status")
def status():
    return render_template('status.html')

@app.route("/test")
def test():
    rows=get_id()
    return render_template('test.html', rows=rows)