# --- Advent of Code 2023 --- 
# --- Day 1: Trebuchet?! ---
#       ____
#     _|____|_
#     ( '<' )
#  >-(   o   )-<
#   (    o    )
#  (     o     )

import re

def read_input(filename):
    input_file = open(filename, 'r')
    input_lst = [line for line in input_file]
    return input_lst


def part1(
    input_lst: list,
) -> int:

    calibration_sum = 0

    for line in input_lst:

        string = line
        nums = ''.join(x for x in string if x.isdigit())
        calibration_number = int(str(nums[0] + nums[-1]))

        calibration_sum = calibration_sum + calibration_number
    
    return(calibration_sum)


def part2(
    input_lst: list,
) -> int:

    conversion_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    calibration_sum = 0

    for line in input_lst:

        numeric_keys = '[0-9]'
        written_keys = '{0}'.format('|'.join(conversion_dict.keys()))
        full_keys = numeric_keys + "|" + written_keys

        pattern = re.compile(r'(?=({0}))'.format(full_keys))
        nums = pattern.findall(line)

        replace_min = ''.join([val for (key, val) in conversion_dict.items() if key in nums[0]])
        replace_max = ''.join([val for (key, val) in conversion_dict.items() if key in nums[-1]])

        nums[0] = nums[0] if replace_min == '' else replace_min
        nums[-1] = nums[-1] if replace_max == '' else replace_max

        calibration_number = int(str(nums[0] + nums[-1]))

        calibration_sum = calibration_sum + calibration_number

    return(calibration_sum)


puzzle_input = read_input('input1.txt')

#Part 1 Solution
part1_solution = part1(puzzle_input)
print("Part 1 Solution: %s"%part1_solution)

#Part 2 Solution
part2_solution = part2(puzzle_input)
print("Part 2 Solution: %s"%part2_solution)