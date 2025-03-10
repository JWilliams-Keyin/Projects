# This program displays the name the user puts into the textbox once they press the button #

# Imports #

from guizero import App, Text, TextBox, PushButton, Slider, Picture

# Functions #

def say_my_name():
  welcome_message.value = my_name.value

def change_text_size(slider_value):
  welcome_message.size = slider_value

# App #

app = App(title = 'Hello World')

welcome_message = Text(app, text = 'Welcome to my app', size = 40, font = "Times new roman", color = 'blue')
my_name = TextBox(app, width = 30)
update_text = PushButton(app, command = say_my_name, text = 'Display my name')
text_size = Slider(app, command = change_text_size, start = 10, end = 80)

cat = Picture(app, image = "cat.jpeg")

app.display()