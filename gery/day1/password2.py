file = open("gery/day1/list")
initlist = []

for i in file:
    initlist.append(i.strip("\n"))
# print(initlist)
state = 0
lst2 = []


#
def right(state, directions, lst2):
    result = state + directions
    if result == 0:
        lst2.append("1")
        print(result, lst2)
        return (result, lst2)
    elif len(str(abs(result))) > 2:
        lst2.append(abs(result) // 100)
        print(result % 100, lst2)
        return (result % 100, lst2)
    else:
        print(abs(result), lst2)
        return (abs(result), lst2)


def left(state, directions, lst2):
    result = state - directions
    if result == 0:
        lst2.append("1")
        print(result, lst2)
        return (result, lst2)
    elif len(str(abs(result))) > 2:
        if (result < 0) and state != 0:
            lst2.append((abs(result) // 100) + 1)
        else:
            lst2.append(abs(result) // 100)
        print(result % 100, lst2)
        return (result % 100, lst2)
    elif result < 0 and state != 0:
        lst2.append("1")
        print(result % 100, lst2)
        return (result % 100, lst2)
    else:
        print(result % 100, lst2)
        return (result % 100, lst2)


password = []
result = 0
init = 50
for y in initlist:
    if y[0] == "R":
        direction = int(y[1:])
        result, lst2 = right(init, direction, lst2)
        init = result
        # print(init)
    if y[0] == "L":
        direction = int(y[1:])
        result, lst2 = left(init, direction, lst2)
        init = result
        # print(init)


int_list = [int(x) for x in lst2]
# print(int_list)

total = sum(int_list)
# print(total)
if __name__ == "__main__":
    print(total)
