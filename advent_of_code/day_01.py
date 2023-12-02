# --- Day 1: Trebuchet?! ---

# -- Aux. functions
# Given a string, it returns all the numbers found in string format.
def get_numbers_from_string(string):
  if len(string) <= 1:
    return string if string.isdigit() else ''
  
  mid_string_len = len(string) // 2
  return get_numbers_from_string(string[:mid_string_len]) + get_numbers_from_string(string[mid_string_len:])


# -- Main Functions

# Puzzle_1.
def trebuchet_input_calibrator(puzzle_input):
  calibration = 0
  with open(puzzle_input, 'r') as input:
    for line in input:
      calibration_value = get_numbers_from_string(line)
      calibration += int(calibration_value[0] + calibration_value[-1])

  return calibration