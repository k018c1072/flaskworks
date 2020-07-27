from flask import Flask, render_template, request

Task06_1 = Flask(__name__)
Task06_1.config['UPLOAD_FOLDER'] = './static/uploads/'


@Task06_1.route('/')
def index():
    return render_template('index06_1.html')


@Task06_1.route('/send', methods=['POST'])
def send():
    img_file = request.files['img_file']
    img_file.save(Task06_1.config['UPLOAD_FOLDER'] + img_file.filename)
    return '<p>画像' + img_file.filename + 'を送信しました</p>'


if __name__ == '__main__':
    Task06_1.debug = True
    Task06_1.run()
