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
    left_days = left_days_time_delta.days
    days = days_time_delta.days

    total_seconds = millis_interval(total_days_time_delta)
    seconds = millis_interval(left_days_time_delta)
    left_percentages = (1 - (seconds / total_seconds)) * 100

    nearly_percentages = math.ceil(left_percentages)
    left_days_for_nearly_percentages = math.floor(total_days * nearly_percentages * 0.01) - days
    floored_left_percentage = math.floor(left_percentages)
    next_nearly_percentages = floored_left_percentage - (floored_left_percentage % 5) + 5
    next_nearly_percentage_days = math.ceil(total_days * next_nearly_percentages * 0.01) - days
    date_for_next_nearly_percentages = (now + timedelta(days=next_nearly_percentage_days)).format('MM/DD')

    if link is None:
        # 미리보기 이미지 생성 및 업로드
        im = generate_text_image((
            f'{days} / {total_days}',
            '{0:.2f} %'.format(left_percentages),
            f'D - {left_days}'
        ))
        output = BytesIO()
        im.save(output, format="png")
        output.seek(0)

        im = imgur_client.upload_from_file(output)
        link = im['link']

    return render_template('index.html', total_days=total_days, left_days=left_days, days=days,
                           left_percentages='{0:.7f}'.format(left_percentages),
                           nearly_percentages=nearly_percentages,
                           left_days_for_nearly_percentages=left_days_for_nearly_percentages,
                           next_nearly_percentages=next_nearly_percentages,
                           date_for_next_nearly_percentages=date_for_next_nearly_percentages,
                           image_link=link)
