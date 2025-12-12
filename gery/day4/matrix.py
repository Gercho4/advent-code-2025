file = open("gery/day4/input")

matrix = []

for i in file:
    matrix.append(list(i.strip()))
# print(matrix[1])

rows = len(matrix)
cols = len(matrix[0])

print(rows, cols)


"""
Function to iterate through each list:
    - check for all the values around the character
    - one with same position above and above +1 and above -1
    - one with same position below and below +1 and below -1
    - one -1 position and one + 1
Exceptions:
    if it's the first list:
        - no positions above
    if it's the last list:
        - no positions below
    if the first character:
        - nothing which is -1
    if it's last character:
        - nothing which is +1
"""

"""
After the comparison:
we need a counter.
So we create a counter and when the counter < 4  we append to a resultlist
"""


def check_rows(row, col, rows, cols):
    count_rolls = 0
    if row > 0 and col > 0:  # Up left
        if (matrix[row - 1])[col - 1] == "@":
            count_rolls += 1
    if row > 0 and col < cols - 1:  # Up right
        if (matrix[row - 1])[col + 1] == "@":
            count_rolls += 1
    if row > 0:
        if (matrix[row - 1])[col] == "@":  # Up
            count_rolls += 1
    if col > 0:
        if (matrix[row])[col - 1] == "@":  # Left
            count_rolls += 1
    if col < cols - 1:
        if (matrix[row])[col + 1] == "@":  # Right
            count_rolls += 1

    if row < rows - 1 and col > 0:
        if (matrix[row + 1])[col - 1] == "@":  # Down Left
            count_rolls += 1

    if row < rows - 1 and col < cols - 1:
        if (matrix[row + 1])[col + 1] == "@":  # Down Right
            count_rolls += 1
    if row < rows - 1:
        if (matrix[row + 1])[col] == "@":  # Down
            count_rolls += 1
    return count_rolls < 4


def check_positions(list):
    rows = len(list)
    cols = len(list[0])
    counter = 0
    for row_i, row in enumerate(list):
        for col_i, char in enumerate(row):
            if char == "@":
                if check_rows(row_i, col_i, rows, cols):
                    counter += 1
    print(counter)
    return counter


check_positions(matrix)
