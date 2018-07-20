# -*- coding: utf-8 -*-
import math
from datetime import timedelta

from arrow import Arrow, now
from flask import render_template

from . import app
from .utils import millis_interval


@app.route('/')
def index():
    start = Arrow(year=2017, month=3, day=15, tzinfo='Asia/Seoul')
    end = Arrow(year=2020, month=1, day=14, tzinfo='Asia/Seoul')
    now_ = now()
    total_days_time_delta = end - start
    left_days_time_delta = end - now_
    days_time_delta = now_ - start

    total_days = total_days_time_delta.days
    left_days = left_days_time_delta.days
    days = days_time_delta.days

    total_seconds = millis_interval(total_days_time_delta)
    seconds = millis_interval(left_days_time_delta)
    left_percentages = (1 - (seconds / total_seconds)) * 100

    nearly_percentages = math.ceil(left_percentages)
    left_days_for_nearly_percentages = math.ceil(total_days * nearly_percentages * 0.01) - days
    floored_left_percentage = math.floor(left_percentages)
    next_nearly_percentages = floored_left_percentage - (floored_left_percentage % 5) + 5
    next_nearly_percentage_days = math.ceil(total_days * next_nearly_percentages * 0.01) - days
    date_for_next_nearly_percentages = (now_ + timedelta(days=next_nearly_percentage_days)).format('MM/DD')
    return render_template('index.html', total_days=total_days, left_days=left_days, days=days,
                           left_percentages='{0:.7f}'.format(left_percentages),
                           nearly_percentages=nearly_percentages,
                           left_days_for_nearly_percentages=left_days_for_nearly_percentages,
                           next_nearly_percentage_days=next_nearly_percentage_days,
                           date_for_next_nearly_percentages=date_for_next_nearly_percentages)
