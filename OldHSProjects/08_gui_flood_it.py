# This program is a puzzle game where the player has to fill up the screen with blue in a limited amount of moves #

# Imports #

from guizero import App, Waffle, Text, PushButton, info
import random

# Variables #

colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'purple']
board_size = 14
moves_limit = 26
moves_taken = 0

# Functions #

def flood(x, y, target, replacement):
  if target == replacement:
    return False
  if board.get_pixel(x, y) != target:
    return False
  board.set_pixel(x, y, replacement)
  if y+1 <= board_size-1:
    flood(x, y+1, target, replacement)
  if y-1 >= 0:
    flood(x, y-1, target, replacement)
  if x+1 <= board_size-1:
    flood(x+1, y, target, replacement)
  if x-1 >= 0:
    flood(x-1, y, target, replacement)

def all_squares_are_the_same():
  squares = board.get_all()
  if all(color == squares[0] for color in squares):
    return True
  else:
    return False

def win_check():
  global moves_taken
  moves_taken += 1
  if moves_taken <= moves_limit:
    if all_squares_are_the_same():
      win_text.value = 'You win!'
  else:
    win_text.value = 'You lose :('

def fill_board():
  for x in range(board_size):
    for y in range(board_size):
      board.set_pixel(x, y, random.choice(colors))

def init_palette():
  for color in colors:
    palette.set_pixel(colors.index(color), 0, color)

def start_flood(x, y):
  flood_color = palette.get_pixel(x, y)
  target = board.get_pixel(0,0)
  flood(0,0, target, flood_color)
  win_check()

# App #

app = App('Flood It')

board = Waffle(app, width = board_size, height = board_size, pad = 0)
palette = Waffle(app, width = 6, height = 1, dotty = True, command = start_flood)
win_text = Text(app)
fill_board()
init_palette()

app.display()