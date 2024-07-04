# This program displays text that flashes and is hard to read #

# Imports #
from guizero import App, Text, TextBox, Combo
from string import ascii_letters

# Functions #
def flash_text():
  if title.visible:
    title.hide()
  else:
    title.show()

# App #
app = App("It's All Gone Wrong!", bg = 'darkgreen')
title = Text(app, text = "Some hard to read text", size = 14, font = 'Comic Sans')

app.repeat(1000, flash_text)

app.display()