# file = open("gery/list")
# initlist = []

# for i in file:
#     initlist.append(i.strip("\n"))
# print(initlist)
# state = 0


# def right(state, directions):
#     # state = int(state)
#     # directions = int(directions)
#     if state + directions > 99 < 999:
#         return (state + directions) % 100
#     elif state + directions > 999:
#         return (state + directions) % 1000
#     else:
#         return state + directions


# def left(state, directions):
#     # state = int(state)
#     # directions = int(directions)
#     if state - directions < 0 > -999:
#         return abs((state - directions) % 100)
#     elif state - directions < -999:
#         return abs((state - directions) % 1000)
#     else:
#         return state - directions


# password = []
# result = 0
# init = 50
# for y in initlist:
#     if y[0] == "R":
#         dir = int(y[1:])
#         result = right(init, dir)
#         init = result
#         print(init)
#         if result == 0:
#             password.append(result)
#         print(init)
#     if y[0] == "L":
#         dir = int(y[1:])
#         result = left(init, dir)
#         init = result
#         print(init)
#         if result == 0:
#             password.append(result)
#         # print(password)
# print(len(password))

# if __name__ == "__main__":
#     print(len(password))
