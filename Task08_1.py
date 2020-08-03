from flask import Flask, render_template
import mysql.connector as db

db_param = {
    'user': 'mysql',
    'host': 'localhost',
    'password': '',
    'database': 'db1'
}

Task08_1 = Flask(__name__)


@Task08_1.route('/')
def index():
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM books'
    cur.execute(stmt)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index08_1.html', books=rows)


if __name__ == "__main__":
    Task08_1.debug = True
    Task08_1.run()
