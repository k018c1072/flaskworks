from flask import Flask, render_template, request
import datetime as dt

Task05_3 = Flask(__name__)

steps_data = []
total_steps = []


@Task05_3.route('/', methods=['POST'])
def send():
    if request.form.get('steps') != '':
        time = dt.datetime.now().strftime("%m/%d %H:%M")
        steps_data.append(time + ' 歩数 : ' + request.form.get('steps'))
        total_steps.append(int(request.form.get('steps')))

    avg = sum(total_steps) / len(total_steps)
    return render_template('index05_3.html', steps_data=steps_data, avg=f'{avg: .1f}')


if __name__ == "__main__":
    Task05_3.debug = True
    Task05_3.run()
