import math
from datetime import timedelta

from arrow import Arrow, now as now_

from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    start = Arrow(year=2017, month=3, day=15)
    end = Arrow(year=2020, month=1, day=14)
    now = now_()
    total_days_time_delta = end - start
    left_days_time_delta = end - now
    days_time_delta = now - start

    total_days = total_days_time_delta.days
    left_days = left_days_time_delta.days
    days = days_time_delta.days

    total_seconds = total_days_time_delta.total_seconds() * 1000
    seconds = left_days_time_delta.total_seconds() * 1000
    left_percentages = (1 - (seconds / total_seconds)) * 100

    nearly_percentages = math.ceil(left_percentages)
    left_days_for_nearly_percentages = math.ceil(total_days * nearly_percentages * 0.01) - days
    floored_left_percentage = math.floor(left_percentages)
    next_nearly_percentages = floored_left_percentage - (floored_left_percentage % 5) + 5
    next_nearly_percentage_days = math.ceil(total_days * next_nearly_percentages * 0.01) - days
    date_for_next_nearly_percentages = (now + timedelta(days=next_nearly_percentage_days)).format('MM/DD')
    return render_template('index.html', total_days=total_days, left_days=left_days, days=days,
                           left_percentages='{0:.7f}'.format(left_percentages),
                           nearly_percentages=nearly_percentages,
                           left_days_for_nearly_percentages=left_days_for_nearly_percentages,
                           next_nearly_percentage_days=next_nearly_percentage_days,
                           date_for_next_nearly_percentages=date_for_next_nearly_percentages)


if __name__ == '__main__':
    app.run()
