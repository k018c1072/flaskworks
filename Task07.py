from flask import Flask, render_template, request, redirect, session
import os

Task07 = Flask(__name__)

Task07.config['SECRET_KEY'] = os.urandom(24)


@Task07.route('/')
def index():
    if 'username' in session:
        return render_template('index07.html', username=str(session['username']))
    else:
        return render_template('login.html')


@Task07.route('/login', methods=['POST'])
def login():
    if request.form.get('username'):
        session['username'] = request.form.get('username')
    return redirect('/')


@Task07.route('/logout')
def logout():
    session.pop('username', None)
    return render_template('login.html')


if __name__ == "__main__":
    Task07.debug = True
    Task07.run()
