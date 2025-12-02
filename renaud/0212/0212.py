"""
python renaud/0212/0212.py
"""


# PART 1
def is_valid_id(id_: str) -> bool:
    if len(id_) % 2 != 0:
        return True
    half_id = id_[: len(id_) // 2]
    return half_id != id_[len(id_) // 2 :]


def check_ranged(input_file: str) -> int:
    with open(input_file, "r") as f:
        lines = f.readlines()
    ranges = [range_.split("-") for range_ in lines[0].strip().split(",")]
    sum_invalid_ids = 0
    for start, end in ranges:
        for id_num in range(int(start), int(end) + 1):
            if not is_valid_id(str(id_num)):
                sum_invalid_ids += id_num
    return sum_invalid_ids


# PART 2
def pattern_repeats_in_an_id(id_: str, pattern_length: int) -> bool:
    if len(id_) % pattern_length != 0:
        return False
    length = len(id_)
    pattern = id_[:pattern_length]
    current_pattern = ""
    for i in range(pattern_length, length - pattern_length + 1, pattern_length):
        current_pattern = id_[i : i + pattern_length]
        if current_pattern != pattern:
            return False
    return True


def is_valid_id_v2(id_: str) -> bool:
    length = len(id_)
    for i in range(1, (length // 2) + 1):
        if pattern_repeats_in_an_id(id_, i):
            return False
    return True


def check_ranged_v2(input_file: str) -> int:
    with open(input_file, "r") as f:
        lines = f.readlines()
    ranges = [range_.split("-") for range_ in lines[0].strip().split(",")]
    sum_invalid_ids = 0
    for start, end in ranges:
        for id_num in range(int(start), int(end) + 1):
            if id_num <= 10:
                continue
            if not is_valid_id_v2(str(id_num)):
                sum_invalid_ids += id_num
    return sum_invalid_ids


if __name__ == "__main__":
    print(f"Result part 1: {check_ranged('renaud/0212/input.txt')}")
    print(f"Result part 2: {check_ranged_v2('renaud/0212/input.txt')}")
