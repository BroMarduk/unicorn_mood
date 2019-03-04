#!/usr/bin/env python

import datetime
import time
import unicornhat as unicorn
import colorconstants

early_warning = colorconstants.colors["yellow1"]
late_warning = colorconstants.colors["orange"]
sleeping = colorconstants.colors["red1"]
awake = colorconstants.colors["green"]
awake_warning = colorconstants.colors["blue"]
normal = colorconstants.colors["black"]
current_color = normal

while True:
    now_date = datetime.datetime.today()
    school_out = datetime.date(datetime.datetime.today().year, 6, 15)
    school_in = datetime.date(datetime.datetime.today().year, 9, 1)
    current_date = datetime.date(now_date.year, now_date.month, now_date.day)
    use_alt = False
    if current_date.weekday() == 5 or current_date.weekday() == 6 or (school_out < current_date < school_in):
        use_alt = True
    early_warning_start = datetime.time(19, 30)
    late_warning_start = datetime.time(19, 50)
    sleeping_start = datetime.time(20, 0)
    awake_start = datetime.time(6, 45) if use_alt == False else datetime.time(8,00)
    awake_warning_start = datetime.time(7, 15) if use_alt == False else datetime.time(8,45)
    awake_normal_start = datetime.time(8, 30) if use_alt == False else datetime.time(9,00)
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
        unicorn.brightness(0.5)
        width,height=unicorn.get_shape()
        red_value, green_value, blue_value = new_color
        for y in range(height):
          for x in range(width):
            unicorn.set_pixel(x, y, red_value, green_value, blue_value)
        current_color = new_color
        unicorn.show()
    time.sleep(1)