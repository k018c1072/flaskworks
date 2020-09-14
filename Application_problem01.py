from flask import Flask, render_template, request, redirect
import mysql.connector as db
import os
import json
import datetime

db_param = {
    'user': 'mysql',
    'host': 'localhost',
    'password': '',
    'database': 'tododb'
}

Application_problem01 = Flask(__name__)


@Application_problem01.route('/')
def index():
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM todolist'
    cur.execute(stmt)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index10.html', todolist=rows)


@Application_problem01.route('/send', methods=['POST'])
def send():
    print(request.files)
    title = request.form.get('title')
    if title == "":
        return redirect('/')
    dt = datetime.datetime.now()
    date = dt.strftime("%y-%m-%d %H:%M")

    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM todolist WHERE title=%s'
    cur.execute(stmt, (title,))
    rows = cur.fetchall()
    if len(rows) == 0:
        cur.execute('INSERT INTO todolist(date, title) VALUES(%s, %s)',
                    (date, title))
    else:
        cur.execute('UPDATE todolist SET date=%s WHERE title=%s',
                    (date, title))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')


@Application_problem01.route('/delete', methods=['POST'])
def delete():
    del_list = request.form.getlist('del_list')
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'DELETE FROM todolist WHERE id=%s'
    for id in del_list:
        cur.execute(stmt, (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')


if __name__ == "__main__":
    Application_problem01.debug = True
    Application_problem01.run()
