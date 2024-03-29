#!/usr/bin/env python

import datetime
import time
import unicornhat as unicorn
import colorconstants

early_warning = colorconstants.colors["goldenrod1"]
# AMY late_warning = purple3
# JAMES late_warning = orange
late_warning = colorconstants.colors["purple3"]
sleeping = colorconstants.colors["red1"]
# AMY awake = deeppink1
# JAMES awake = green1
awake = colorconstants.colors["deeppink1"]
awake_warning = colorconstants.colors["blue"]
normal = colorconstants.colors["black"]
current_color = normal

while True:
    now_date = datetime.datetime.today()
    school_out = datetime.date(datetime.datetime.today().year, 6, 15)
    school_in = datetime.date(datetime.datetime.today().year, 8, 29)
    current_date = datetime.date(now_date.year, now_date.month, now_date.day)
    use_non_school_mornings = False
    if current_date.weekday() == 5 or current_date.weekday() == 6 or (school_out < current_date < school_in):
        use_non_school_mornings = True
    use_non_school_evenings = False
    if current_date.weekday() == 4 or current_date.weekday() == 5 or (school_out < current_date < school_in):
        use_non_school_evenings = True
    early_warning_start = datetime.time(19, 30) if use_non_school_evenings is False else datetime.time(20, 00)
    late_warning_start = datetime.time(19, 50) if use_non_school_evenings is False else datetime.time(20, 20)
    sleeping_start = datetime.time(20, 00) if use_non_school_evenings is False else datetime.time(20, 30)
    awake_start = datetime.time(6, 30) if use_non_school_mornings is False else datetime.time(8, 00)
    awake_warning_start = datetime.time(7, 40) if use_non_school_mornings is False else datetime.time(8, 45)
    awake_normal_start = datetime.time(8, 00) if use_non_school_mornings is False else datetime.time(9, 00)
    new_color = current_color
    now_time = datetime.datetime.now()
    current_time = datetime.time(now_time.hour, now_time.minute)
    if early_warning_start <= current_time < late_warning_start:
        new_color = early_warning
    elif late_warning_start <= current_time < sleeping_start:
        new_color = late_warning
    elif sleeping_start <= current_time or current_time < awake_start:
        new_color = sleeping
    elif awake_start <= current_time < awake_warning_start:
        new_color = awake
    elif awake_warning_start <= current_time < awake_normal_start:
        new_color = awake_warning
    else:
        new_color = normal
    if new_color != current_color:
        unicorn.set_layout(unicorn.AUTO)
        unicorn.rotation(0)
        unicorn.brightness(0.4 if new_color == sleeping else 1)
        width, height = unicorn.get_shape()
        red_value, green_value, blue_value = new_color
        for y in range(height):
            for x in range(width):
                unicorn.set_pixel(x, y, red_value, green_value, blue_value)
        current_color = new_color
        unicorn.show()
    time.sleep(1)
