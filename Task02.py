from flask import Flask
import datetime


Task02 = Flask(__name__)


@Task02.route('/')
def now_time():
    dt = datetime.datetime.now()
    return dt.strftime('%m/%d %H:%M')


if __name__ == '__main__':
    Task02.debug = True
    Task02.run()
