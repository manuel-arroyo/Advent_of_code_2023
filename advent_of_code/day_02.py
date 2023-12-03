# --- Day 1: Trebuchet?! ---
import fileinput
from functools import reduce

# -- Aux. functions
# Recursive method, returns if the game matchs all the colors costraints given
def is_game_valid(game, game_constraints):
  current_game = game.split('; ')
  if len(current_game) <= 1:
    return all(map(lambda game: int(game.split(' ')[0]) <= game_constraints[game.split(' ')[1]],current_game[0].split(', ')))
  
  mid_game_len = len(current_game) // 2
  return all([is_game_valid('; '.join(current_game[:mid_game_len]), game_constraints), is_game_valid('; '.join(current_game[mid_game_len:]), game_constraints)])


def min_game_constraints(game):
  min_constraints = {}
  current_game = game.split('; ')
  if len(current_game) <= 1:
    for game in current_game[0].split(', '):
      min_constraints[game.split(' ')[1]] =  int(game.split(' ')[0])
    
    return min_constraints
  
  mid_game_len = len(current_game) // 2
  min_constraints = min_game_constraints('; '.join(current_game[:mid_game_len]))
  right_game_constraints = min_game_constraints('; '.join(current_game[mid_game_len:]))
  for key in right_game_constraints.keys():
    if key in min_constraints:
      min_constraints[key] = right_game_constraints[key] if right_game_constraints[key] > min_constraints[key] else min_constraints[key]
    else:
      min_constraints[key] = right_game_constraints[key]
  
  return min_constraints


# -- Main Functions
def main():
    games_logs: list[str] = list(map(str.rstrip, fileinput.input()))
    
    print(get_valid_games(games_logs))
    print(get_min_games_cosntraints_sum(games_logs))
    
# Puzzle_1.
def get_valid_games(game_input):
  game_constraints = {
    'red': 12,
    'green': 13,
    'blue': 14
  }
  
  valid_games = sum(map(lambda game: int(game.split(': ')[0].split('Game ')[1]), filter(lambda game: is_game_valid(game.split(': ')[1], game_constraints), game_input)))
  return valid_games

# Puzzle_1.
def get_min_games_cosntraints_sum(game_input):
  multiply_list = lambda list: reduce(lambda x, y: x * y, list) 
  valid_games = sum(map(multiply_list , list(map(lambda game: list(min_game_constraints(game.split(': ')[1]).values()), game_input))))
  return valid_games


if __name__ == '__main__':
    main()