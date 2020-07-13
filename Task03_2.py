from flask import Flask, render_template

Task03_2 = Flask(__name__)


@Task03_2.route('/')
def index():
    return render_template('index03_2.html', test={'英語': 87, '数学': 90, '国語': 45, '理科': 76, '社会': 31})


if __name__ == '__main__':
    Task03_2.debug = True
    Task03_2.run()
