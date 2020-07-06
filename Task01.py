from flask import Flask

Task01 = Flask(__name__)


@Task01.route('/')
def top_page():
    return 'トップページ'


if __name__ == '__main__':
    Task01.debug = True
    Task01.run()
