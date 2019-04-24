import random
from pprint import pprint

# real board
EMPTY = 0
MINE = 1

FLAG = 11
UNKNOWN = 12

# actions
A_COVER = 0
A_UNCOVER = 1
A_FLAG = 2


alphabet = 'abcdefghijklmnopqrstuvwxyz'

real_board = None
shown_board = None

MINE_CHANCE = 0.12

BOARD_SIZE = 9

def is_mine():
  pass

def count_adjacent():
  pass

def create_board(size=BOARD_SIZE, difficulty='easy'):
  global BOARD_SIZE
  global real_board
  global shown_board
  BOARD_SIZE = size
  real_board = [[0 for i in range(size)] for i in range(size)]
  shown_board = [[0 for i in range(size)] for i in range(size)]

  options = [EMPTY,MINE]
  weights = [1.0 - MINE_CHANCE, MINE_CHANCE]
  # print('choice', random.choices(options, weights))
  for i in range(size):
    for j in range(size):
      value = random.choices(options, weights)[0]
      real_board[i][j] = value

  # pprint(real_board)
  # pprint(shown_board)

def get_input():
  i = input('move> ')
  i = i.split(' ')
  action = i[0]
  location = i[1]
  return 

def update():
  return True

def render():
  b = ''

  b += '  '
  for col in range(BOARD_SIZE):
      b += str(col) + ' '
  b += '\n'
  for row in range(BOARD_SIZE):
    b += alphabet[row] + ' '
    for col in range(BOARD_SIZE):
      value = 
      b += str(shown_board[row][col]) + ' '
    b += '\n'
    
  print(b)

def get_value(cell):
  pass

def main():
  create_board()
  running = True
  while running:
    render()
    get_input()
    running = update()

if __name__ == '__main__':
  main()