# This program allows the user to input the date in a very annoying way #

# Imports #
from guizero import App, Slider, Text
from time import ctime

# Functions #
def update_date():
  the_date.value= ctime(date_slider.value)

# App #
app = App('Set the date with the slider')

the_date = Text(app)
date_slider = Slider(app, start = 0, end = 9999999999, command = update_date)

app.display()