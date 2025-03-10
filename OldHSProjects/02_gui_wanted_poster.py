# This program displays an image of a wanted dog #

# Imports #

from guizero import App, Text, Picture

# App #

app = App('Wanted!')
app.bg = '#FBFBD0'
app.bg = (251, 251, 208)

wanted_text = Text(app, text = 'WANTED')
wanted_text.text_size = 50

dog = Picture(app, image = 'dog.jpg')
dog.image_size = 1

app.display()