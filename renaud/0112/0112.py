"""
python renaud/0112.py
"""


class IntegerMod99:
    def __init__(self, value: int):
        self.value = value % 100
        self.abs_quotient = abs(value // 100)

    def __add__(self, other):
        if isinstance(other, IntegerMod99):
            return IntegerMod99(self.value + other.value)
        if isinstance(other, int):
            return IntegerMod99(self.value + other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, IntegerMod99):
            return IntegerMod99(self.value - other.value)
        if isinstance(other, int):
            return IntegerMod99(self.value - other)
        return NotImplemented

    def __repr__(self):
        return f"IntegerMod99({self.value}, abs_quotient={self.abs_quotient})"


def enter_combinations(input_path: str) -> int:
    with open(input_path, "r") as file:
        lines = file.readlines()

    count_on_0 = 0
    position = IntegerMod99(50)
    for line in lines:
        line = line.strip()
        direction = line[0]
        number = int(line[1:])
        if direction == "L":
            position -= number
        elif direction == "R":
            position += number
        if position.value == 0:
            count_on_0 += 1
    return count_on_0


def enter_combinations_method_0x434C49434B(input_path: str) -> int:
    with open(input_path, "r") as file:
        lines = file.readlines()

    count_passed_on = 0
    position = IntegerMod99(50)
    for line in lines:
        line = line.strip()
        direction = line[0]
        number = int(line[1:])
        count_passed_on += abs(number) // 100
        remainder = number % 100
        if direction == "L":
            if position.value <= remainder and position.value != 0:
                count_passed_on += 1
            position = position - remainder
        if direction == "R":
            if position.value + remainder >= 100 and position.value != 0:
                count_passed_on += 1
            position = position + remainder

    return count_passed_on


if __name__ == "__main__":
    result = enter_combinations("renaud/0112_input.txt")
    print(f"Result first part: {result}")

    result_2 = enter_combinations_method_0x434C49434B("renaud/0112_input.txt")
    print(f"Result second part: {result_2}")
