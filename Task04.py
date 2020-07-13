from flask import Flask, render_template

Task04 = Flask(__name__)

users = []


@Task04.route('/user/<username>/')
def useradd(username):
    users.append(username)
    return render_template('useradd.html', username=username)


@Task04.route('/list/')
def userslist():
    return render_template('userslist.html', users=users)


if __name__ == '__main__':
    Task04.debug = True
    Task04.run()
