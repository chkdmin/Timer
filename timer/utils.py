# -*- coding: utf-8 -*-
def millis_interval(diff):
    """start and end are datetime instances"""
    millis = diff.days * 24 * 60 * 60 * 1000
    millis += diff.seconds * 1000
    millis += diff.microseconds / 1000
    return millis
