file = open("gery/day1/list")
initlist = []

for i in file:
    initlist.append(i.strip("\n"))
# print(initlist)
state = 0
lst2 = []


#
def right(state, directions, lst2):
    res = state + directions
    if 99 < res < 999:
        forthelist = str(abs(res))
        if len(forthelist) < 3:
            lst2.append("1")
        else:
            lst2.append(forthelist[0])
        print(forthelist)
        print(lst2)
        res = res % 100
        return (res, lst2)
    elif res > 999:
        forthelist = str(abs(res))
        print(forthelist)
        lst2.append(forthelist[:2])
        print(lst2)
        res = res % 1000
        return (res, lst2)
    else:
        print(res)
        print(lst2)
        return res, lst2


def left(state, directions, lst2):
    res = state - directions
    if 0 > res > -999:
        print(res)
        forthelist = str(abs(res))
        if len(forthelist) < 3:
            lst2.append("1")
        else:
            lst2.append(forthelist[0])
        print(lst2)
        res = abs(res % 100)
        print(res)
        return (res, lst2)
    elif res < -999:
        forthelist = str(abs(res))
        print(forthelist)
        lst2.append(forthelist[:2])
        print(lst2)
        res = abs(res % 1000)
        return (res, lst2)
    else:
        print(res)
        print(lst2)
        return res, lst2


password = []
result = 0
init = 50
for y in initlist:
    if y[0] == "R":
        dir = int(y[1:])
        result, lst2 = right(init, dir, lst2)
        init = result
        print(init)
        if result == 0:
            password.append(result)
        # print(init)
    if y[0] == "L":
        dir = int(y[1:])
        result, lst2 = left(init, dir, lst2)
        init = result
        print(init)
        if result == 0:
            password.append(result)
        print(password)

int_list = [int(x) for x in lst2]
print(int_list)

total = len(password) + sum(int_list)
print(total)
# if __name__ == "__main__":
#     print(len(password))
