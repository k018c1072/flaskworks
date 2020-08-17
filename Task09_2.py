from flask import Flask, render_template, request, redirect
import mysql.connector as db
import os
import json

db_param = {
    'user': 'mysql',
    'host': 'localhost',
    'password': '',
    'database': 'itemdb'
}

Task09_2 = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
Task09_2.config['UPLOAD_FOLDER'] = './static/uploads'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@Task09_2.route('/')
def index():
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM list'
    cur.execute(stmt)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index09_2.html', list=rows)


if __name__ == "__main__":
    Task09_2.debug = True
    Task09_2.run()
