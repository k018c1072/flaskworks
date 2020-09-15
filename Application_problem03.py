from flask import Flask, render_template, request, redirect
import mysql.connector as db
import os
import json
import datetime

db_param = {
    'user': 'mysql',
    'host': 'localhost',
    'password': '',
    'database': 'usertododb'
}

user = ""

Application_problem03 = Flask(__name__)


@Application_problem03.route('/')
def index():
    return render_template('login.html')


@Application_problem03.route('/signUp')
def signUp():
    return render_template('signUp.html')


@Application_problem03.route('/create', methods=['POST'])
def create():
    global user
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
        user = id
        cur.execute('INSERT INTO users(id, pw) VALUES(%s, %s)',
                    (id, pw))
        conn.commit()
        stmt = 'SELECT * FROM todolist WHERE user=%s'
        cur.execute(stmt, (user,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('userPage.html', name=user, todolist=rows)
    else:
        cur.close()
        conn.close()
        return render_template('signUp.html')


@Application_problem03.route('/login', methods=['POST'])
def login():
    global user
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
    if len(rows) != 0:
        user = id
        stmt = 'SELECT * FROM todolist WHERE user=%s'
        cur.execute(stmt, (user,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return render_template('userpage.html', name=user, todolist=rows)
    else:
        return redirect('/')


@Application_problem03.route('/send', methods=['POST'])
def send():
    global user
    title = request.form.get('title')
    if title == "":
        return render_template('userPage.html', name=user)
    dt = datetime.datetime.now()
    date = dt.strftime("%y-%m-%d %H:%M")

    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM todolist WHERE title=%s and user=%s'
    cur.execute(stmt, (title,  user))
    rows = cur.fetchall()
    if len(rows) == 0:
        cur.execute('INSERT INTO todolist(date, title, user) VALUES(%s, %s, %s)',
                    (date, title, user))
    else:
        cur.execute('UPDATE todolist SET date=%s WHERE title=%s and user=%s',
                    (date, title,  user))
    conn.commit()
    stmt = 'SELECT * FROM todolist WHERE user=%s'
    cur.execute(stmt, (user,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('userPage.html', name=user, todolist=rows)


@Application_problem03.route('/delete', methods=['POST'])
def delete():
    global user
    del_list = request.form.getlist('del_list')
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'DELETE FROM todolist WHERE id=%s'
    for id in del_list:
        cur.execute(stmt, (id,))
    conn.commit()
    stmt = 'SELECT * FROM todolist WHERE user=%s'
    cur.execute(stmt, (user,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('userPage.html', name=user, todolist=rows)


if __name__ == "__main__":
    Application_problem03.debug = True
    Application_problem03.run()
