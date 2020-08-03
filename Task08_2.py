from flask import Flask, render_template, request, redirect
import mysql.connector as db

db_param = {
    'user': 'mysql',
    'host': 'localhost',
    'password': '',
    'database': 'db1'
}

Task08_2 = Flask(__name__)


@Task08_2.route('/')
def index():
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM books'
    cur.execute(stmt)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index08_2.html', books=rows)


@Task08_2.route('/send', methods=['POST'])
def send():
    title = request.form.get('title')
    price = request.form.get('price')
    if title == "" or price == "":
        return redirect('/')
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'INSERT INTO books(title, price) VALUES(%s, %s)'
    cur.execute(stmt, (title, int(price)))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')


if __name__ == "__main__":
    Task08_2.debug = True
    Task08_2.run()
