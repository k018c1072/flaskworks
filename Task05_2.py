from flask import Flask, render_template, request
import datetime as dt

Task05_2 = Flask(__name__)

steps_data = []


@Task05_2.route('/', methods=['POST'])
def send():
    if request.form.get('steps') != '':
        time = dt.datetime.now().strftime("%m/%d %H:%M")
        steps_data.append(time + ' 歩数 : ' + request.form.get('steps'))
    return render_template('index05_2.html', steps_data=steps_data)


if __name__ == "__main__":
    Task05_2.debug = True
    Task05_2.run()
