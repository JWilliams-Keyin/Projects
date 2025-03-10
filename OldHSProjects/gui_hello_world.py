from guizero import App, PushButton, Slider, Text

def say_hello():
  text.value = 'Hello world'

app = App(title = 'Hello World')
text = Text(app)
message = Text(app, text = 'Welcome to the Hello World app!')
button = PushButton(app, command = say_hello)
app.display()