file = open("gery/day2/rangelist")
fileread = file.read()
rangelist = fileread.split(",")
# print(rangelist)
range_dict = {}

for a in rangelist:
    range_min, range_max = a.split("-")
    range_dict[int(range_min)] = int(range_max)
# print(range_dict)

#     print(a, b)
# # result_list = [for a, b in (item.split("-") for item in rangelist)]
# # print(rangelist)


def detect_twins(input_range):
    for range_min, range_max in input_range.items():
        # print(range_min, range_max)
        for i in range(range_min, range_max):
            try:
                # print(i)
                string_num = str(i)
                if len(string_num) % 2 == 0:
                    mid = len(string_num) // 2
                    left = int(string_num[:mid])
                    right = int(string_num[mid:])
                    if left == right:
                        # print("Twin found:", i)
                        result_list.append(i)
                else:
                    continue
            except Exception as e:
                print("Error at number", i, ":", e)
                continue
    print(result_list)
    print(sum(result_list))
    print
    return result_list


result_list = []
detect_twins(range_dict)
