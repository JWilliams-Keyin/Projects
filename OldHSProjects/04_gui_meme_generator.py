# This program generates a meme that the user can customize #

# Imports #

from guizero import App, TextBox, Drawing, Combo, Slider

# Functions #

def draw_meme():
  meme.clear()
  meme.image(0,0, 'meme_generator_picture.jpg', width = 500, height = 500)
  meme.text(20,20, top_text.value, color = color1.value, font = font.value,size = size1.value)
  meme.text(20,450, bottom_text.value, color = color2.value, font = font.value, size = size2.value)
    
# App #

app = App('meme')

top_text = TextBox(app, 'top text', command = draw_meme)
bottom_text = TextBox(app, 'bottom text', command = draw_meme)
color1 = Combo(app, options = ['black', 'white', 'gray', 'green', 'blue', 'orange', 'purple', 'pink'], command = draw_meme)
color2 = Combo(app, options = ['black', 'white', 'gray', 'red', 'green', 'blue', 'orange', 'purple', 'pink'], command = draw_meme)
font = Combo(app, options = ['times new roman', 'verdana', 'courier', 'impact'], command = draw_meme)
size1 = Slider(app, start = 20, end = 40, command = draw_meme)
size2 = Slider(app, start = 20, end = 40, command = draw_meme)
meme = Drawing(app, width = 'fill', height = 'fill')

draw_meme()
app.display()