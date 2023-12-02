# --- Day 1: Trebuchet?! ---

# -- Aux. functions
# Given a string, it returns all the numbers found in string format.
def get_numbers_from_string(string):
  if len(string) <= 1:
    return string if string.isdigit() else ''
  
  mid_string_len = len(string) // 2
  return get_numbers_from_string(string[:mid_string_len]) + get_numbers_from_string(string[mid_string_len:])

# Parser spelled numbers. Returns numeric in string format.
def parse_spelled_numbers(string):
  numbers = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e'
  }
  for key in numbers.keys():
      for n in range(string.count(key)):
        string = string.replace(key, numbers[key])
  
  return string


# -- Main Functions
# Puzzle_1.
def trebuchet_input_calibrator(puzzle_input, num_parser=False):
  calibration = 0
  with open(puzzle_input, 'r') as input:
    for line in input:
      line = parse_spelled_numbers(line) if num_parser else line
      calibration_value = get_numbers_from_string(line)
      calibration_value = calibration_value if len(calibration_value) > 0 else 0
      calibration += int(calibration_value[0] + calibration_value[-1])
  
  return calibration
      
# Puzzle_2.
def trebuchet_input_calibrator_with_number_parser(puzzle_input):
  return trebuchet_input_calibrator(puzzle_input, True)