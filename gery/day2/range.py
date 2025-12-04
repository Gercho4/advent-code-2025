file = open("gery/day2/rangelist")
fileread = file.read()
rangelist = fileread.split(",")
print(rangelist)
for i in rangelist:
    functions


def detect_twins(input_range):
    range_min, range_max = map(int, input_range.split("-"))
    for i in range(range_min, range_max):
        