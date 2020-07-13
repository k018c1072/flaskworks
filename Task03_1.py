from flask import Flask, render_template

Task03_1 = Flask(__name__)


@Task03_1.route('/')
def index():
    return render_template('index.html', num=10)


if __name__ == '__main__':
    Task03_1.debug = True
    Task03_1.run()
