# This program is a simple game if tic tac toe #

# Imports #

from guizero import App, Box, PushButton, Text

# Functions #

def clear_board():
  new_board = [[None, None, None], [None, None, None], [None, None, None]]
  for x in range(3):
    for y in range(3):
      button = PushButton(board, text = '', grid = [x, y], width = 3, command = choose_square, args = [x,y])
      new_board[x][y] = button
  return new_board

def choose_square(x, y):
  board_squares[x][y].text = turn
  board_squares[x][y].disable()
  toggle_player()
  check_win()

def toggle_player():
  global turn
  if turn == 'X':
    turn = 'O'
  else:
    turn = 'X'
  message.value = 'It is your turn, ' + turn
  
def check_win():
  winner = None

  # Vertical Lines #

  if (board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text) and board_squares [0][2].text in ['X', 'O']:
    winner = board_squares[0][0]
  elif (board_squares[1][0].text == board_squares[1][1].text == board_squares[1][2].text) and board_squares [1][2].text in ['X', 'O']:
    winner = board_squares[1][0]
  elif (board_squares[2][0].text == board_squares[2][1].text == board_squares[2][2].text) and board_squares [2][2].text in ['X', 'O']:
    winner = board_squares[2][0]

    # Horizontal Lines #
  elif (board_squares[0][0].text == board_squares[1][0].text == board_squares[2][0].text) and board_squares [2][0].text in ['X', 'O']:
    winner = board_squares[0][0]
  elif (board_squares[0][1].text == board_squares[1][1].text == board_squares[2][1].text) and board_squares [1][2].text in ['X', 'O']:
    winner = board_squares[0][1]
  elif (board_squares[0][2].text == board_squares[1][2].text == board_squares[2][2].text) and board_squares [2][2].text in ['X', 'O']:
    winner = board_squares[0][2]

    # Diagonal Lines #
  elif (board_squares[0][0].text == board_squares[1][1].text == board_squares[2][2].text) and board_squares [2][2].text in ['X', 'O']:
    winner = board_squares[0][0]
  elif (board_squares[0][2].text == board_squares[1][1].text == board_squares[2][0].text) and board_squares [2][0].text in ['X', 'O']:
    winner = board_squares[0][2]
  
  if winner is not None:
    message.value = winner.text + ' wins!'
  elif moves_taken() == 9:
    message.value = 'It is a draw'

def moves_taken():
  moves = 0
  for row in board_squares:
    for col in row:
      if col.text == 'X' or col.text == 'O':
        moves = moves + 1
  return moves

# Variables #

turn = 'X'

# App #

app = App('Tic Tac Toe')
board = Box(app, layout = 'grid')
board_squares = clear_board()
message = Text(app, text = 'It is your turn, ' + turn)

app.display()