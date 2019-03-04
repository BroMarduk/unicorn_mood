#!/usr/bin/env python

import time
import unicornhat as unicorn
import sys
import getopt
import colorconstants

red_value = 0
green_value  = 255
blue_value = 0

try:
  options, args = getopt.getopt(sys.argv[1:], 'hr:g:b:c:x:', ['red=', 'green=', 'blue=', 'color=', 'hex='])
except getopt.GetoptError:
  print('set-unicorn-color.py -r <red value> -g <green value> -b <blue value>')
  print('set-unicorn-color.py -c <defined color name>')
  print('set-unicorn-color.py -x <color hex code>')
  sys.exit(2)

for option, arg in options:
  if option == '-h':
    print('set-unicorn-color.py -r <red value> -g <green value> -b <blue value>')
    print('set-unicorn-color.py -c <defined color name>')
    print('set-unicorn-color.py -x <color hex code>')
    sys.exit()
  elif option in ("-r", "--red"):
     red_value = arg
  elif option in ("-g", "--green"):
     green_value = arg
  elif option in ("-b", "--blue"):
     blue_value = arg
  elif option in ("-c", "--color"):
     red_value, green_value, blue_value = colorconstants.colors[arg]


unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(0)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()

for y in range(height):
  for x in range(width):
    unicorn.set_pixel(x, y, red_value, green_value, blue_value)

unicorn.show()

while True:
    time.sleep(1)