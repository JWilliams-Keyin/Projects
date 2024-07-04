# This program displays a useless message saying that the app is started #

# Imports #

from guizero import App, PushButton

# Functions #

def are_you_sure():
  if app.yesno('Confirmation', 'Are you sure?'):
     app.info('Thanks', 'Button pressed')
  else:
    app.error('Ok', 'Cancelling')

# App #

app = App(title = 'pointless pop-ups')

button = PushButton(app, command = are_you_sure)

app.info('Application started', 'Well done you started the application')

app.display()