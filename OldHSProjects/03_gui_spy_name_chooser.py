# This program gives the user a spy name when the button is pressed #

# Imports #

from guizero import App, Text, Picture, PushButton
from random import choice

# Functions #

def choose_name():
  #print('Button was pressed')
  first_names = ['Bob', 'Becky', 'Jim', 'Jess', 'Charlie', 'Mia']
  last_names = ['Wolfbrand', 'Wavybottom', 'Trollsbreath', 'Littlefoot', 'Replpants', 'Slitherman']
  spy_name = choice(first_names) + ' ' + choice(last_names)
  print(spy_name)

# App #

app = App('TOP SECRET')
title = Text(app, text = "Push the red button to find out your spy name")
button = PushButton(app, choose_name, text = 'Tell Me!')
name = Text(app, text = '')

app.display()