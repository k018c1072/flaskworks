from flask import Flask, render_template, request

Task06_2 = Flask(__name__)
Task06_2.config['UPLOAD_FOLDER'] = './static/uploads/'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@Task06_2.route('/')
def index():
    return render_template('index06_1.html')


@Task06_2.route('/send', methods=['POST'])
def send():
    img_file = request.files['img_file']
    if img_file and allowed_file(img_file.filename):
        img_file.save(Task06_2.config['UPLOAD_FOLDER'] + img_file.filename)
        return '<p>画像' + img_file.filename + 'を送信しました</p>'
    else:
        return '<p>許可されていない拡張子です</p>'


if __name__ == '__main__':
    Task06_2.debug = True
    Task06_2.run()
