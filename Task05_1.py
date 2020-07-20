from flask import Flask, render_template, request

Task05_1 = Flask(__name__)


@Task05_1.route('/')
def index():
    return render_template('index05_1.html')


@Task05_1.route('/send', methods=['POST'])
def send():
    name = request.form.get('name')
    mail = request.form.get('mail')
    return render_template('receive05_1.html', name=name, mail=mail)


if __name__ == "__main__":
    Task05_1.debug = True
    Task05_1.run()
