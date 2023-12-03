# --- Day 1: TESTS ---
from advent_of_code import day_02

def test_puzzle_1():
    assert day_02.trebuchet_input_calibrator('/home/marroyo/Advent_of_code_2023/inputs/day_01/day_01_1_base.txt') == 142
    
def test_puzzle_2():
    assert day_01.trebuchet_input_calibrator_with_number_parser('/home/marroyo/Advent_of_code_2023/inputs/day_01/day_01_2_base.txt') == 281