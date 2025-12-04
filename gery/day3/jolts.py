# - add to list
file = open("gery/day3/input")
initlist = []
resultlist = []
for i in file:
    initlist.append(i.strip("\n"))
# print(initlist)


def detect_biggest(initlist):
    for i in initlist:
        try:
            one = max(i[:-1])
            # print("The first digit is", one)
            split_number = i.split(one, 1)[1:]

            # print("Split number is:", split_number)
            two = max(split_number[0])
            # print("The second digit is", two)
            # print(one, two)
        except Exception as e:
            print("Error at number", i, ":", e)
            continue
        number = one + two
        resultlist.append(number)
        # print(number)
        # number = text.replace(" ", "")
    return number


detect_biggest(initlist)
resultlist = [int(x) for x in resultlist]
print(sum(resultlist))
