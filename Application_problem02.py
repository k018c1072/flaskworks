from flask import Flask, render_template, request, redirect
import mysql.connector as db
import os
import json
import datetime

db_param = {
    'user': 'mysql',
    'host': 'localhost',
    'password': '',
    'database': 'userdb'
}

Application_problem02 = Flask(__name__)


@Application_problem02.route('/')
def index():
    return render_template('login.html')


@Application_problem02.route('/signUp')
def signUp():
    return render_template('signUp.html')


@Application_problem02.route('/create', methods=['POST'])
def create():
    id = request.form.get('name')
    pw = request.form.get('password')
    if id == "" or pw == "":
        return redirect('/')
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM users WHERE id=%s'
    cur.execute(stmt, (id,))
    rows = cur.fetchall()

    if len(rows) == 0:
        cur.execute('INSERT INTO users(id, pw) VALUES(%s, %s)',
                    (id, pw))
        conn.commit()
        cur.close()
        conn.close()
        return render_template('userPage.html', name=id)
    else:
        cur.close()
        conn.close()
        return render_template('signUp.html')


@Application_problem02.route('/login', methods=['POST'])
def login():
    id = request.form.get('name')
    pw = request.form.get('password')
    if id == "" or pw == "":
        return redirect('/')
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM users WHERE id=%s and pw=%s'
    cur.execute(stmt, (id, pw))
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()
    if len(rows) != 0:
        return render_template('userpage.html', name=id)
    else:
        return redirect('/')


if __name__ == "__main__":
    Application_problem02.debug = True
    Application_problem02.run()
