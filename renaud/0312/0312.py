"""
python renaud/0312/0312.py
"""


# Part 1
def highest_combination(bank: str) -> int:
    """
    Take some numbers and return the highest two number combination.

    "818181911112111" -> 92
    """
    max_decimal = 0
    max_integer = 0
    for i in range(len(bank) - 1):
        current_number = int(bank[i])
        if current_number <= max_decimal:
            continue
        else:
            max_decimal = current_number
        for j in range(i + 1, len(bank)):
            next_number = int(bank[j])
            combination = current_number * 10 + next_number
            if combination > max_integer:
                max_integer = combination
    return max_integer


def count_voltage(input_path: str) -> int:
    with open(input_path, "r") as file:
        lines = file.readlines()

    return sum(highest_combination(line.strip()) for line in lines)


# Part 2
def highest_combination_twelve(bank: str) -> int:
    """
    Take some numbers and return the highest twelve number combination.

    "818181911112111" -> 888911112111
    """
    current_left_position = 0
    current_right_position = len(bank) - 1 - 11
    final_number_in_string = ""
    for _ in range(12):
        max_number = -1
        for j in range(current_left_position, current_right_position + 1):
            current_number = int(bank[j])
            if current_number > max_number:
                max_number = current_number
                max_index = j
        final_number_in_string += str(max_number)
        current_left_position = max_index + 1
        current_right_position += 1
    return int(final_number_in_string)


def count_voltage_part_2(input_path: str) -> int:
    with open(input_path, "r") as file:
        lines = file.readlines()

    return sum(highest_combination_twelve(line.strip()) for line in lines)


if __name__ == "__main__":
    result_test = count_voltage("renaud/0312/input_test.txt")
    print(f"Test result: {result_test}")

    result = count_voltage("renaud/0312/input.txt")
    print(f"Result: {result}")

    result_test_2 = count_voltage_part_2("renaud/0312/input_test.txt")
    print(f"Test result part 2: {result_test_2}")

    result_2 = count_voltage_part_2("renaud/0312/input.txt")
    print(f"Result part 2: {result_2}")
