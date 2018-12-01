# -*- coding: utf-8 -*-
import math
from datetime import timedelta
from io import BytesIO

import arrow
from flask import render_template

from . import app, imgur_client
from .utils import millis_interval, generate_text_image

link = None


@app.route('/')
def index():
    global link
    start = arrow.get(app.config['START_DATE_STRING']).replace(tzinfo='Asia/Seoul')
    end = arrow.get(app.config['END_DATE_STRING']).replace(tzinfo='Asia/Seoul')
    now = arrow.now()
    total_days_time_delta = end - start
    left_days_time_delta = end - now
    days_time_delta = now - start

    total_days = total_days_time_delta.days
    left_days = (left_days_time_delta.days + 1)
    if left_days <= 0:
        return render_template("finish.html", left_days=(left_days * -1))
    days = days_time_delta.days

    total_seconds = millis_interval(total_days_time_delta)
    seconds = millis_interval(left_days_time_delta)
    left_percentages = (1 - (seconds / total_seconds)) * 100

    nearly_percentages = math.ceil(left_percentages)
    percentages_data = []
    for percentage in range(int(nearly_percentages), 101):
        left_day_of_percentages = math.floor(total_days * percentage * 0.01) - days
        percentages_date = now + timedelta(days=left_day_of_percentages)
        percentages_data.append(
            dict(percentage=percentage,
                 left_day_of_percentages=left_day_of_percentages,
                 percentages_date=percentages_date.format('YYYY. MM.DD'))
        )

    if link is None:
        # 미리보기 이미지 생성 및 업로드
        im = generate_text_image((
            f'{days} / {total_days}',
            '{0:.2f}%'.format(left_percentages) + f' (D - {left_days})',
            f'{percentages_data[0]["percentage"]}% on {percentages_data[0]["percentages_date"]} (D-{percentages_data[0]["left_day_of_percentages"]})'
        ))
        output = BytesIO()
        im.save(output, format="png")
        output.seek(0)

        im = imgur_client.upload_from_file(output)
        link = im['link']

    return render_template('index.html', total_days=total_days, left_days=left_days, days=days,
                           left_percentages='{0:.7f}'.format(left_percentages),
                           percentages_data=percentages_data,
                           image_link=link)
