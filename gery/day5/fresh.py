# Fresh or Spolied
# Split before and after the newline
#
# After that for i in product_list is it in (iterate all ranges)
#
file = open("gery/day5/input")
product_list = []
fresh_ranges = []
full_list = []
for i in file:
    full_list.append(i.strip("\n"))

# print(full_list)

indices = [i for i, value in enumerate(full_list) if value == ""]
my_split_nr = indices[0]
# print(my_split_nr)


product_list = full_list[my_split_nr + 1 :]
fresh_ranges = full_list[:my_split_nr]
print(product_list)
print(fresh_ranges)


def check_in_range(product_list, fresh_ranges):
    counter = []
    for i in product_list:
        # print(i)
        for y in fresh_ranges:
            my_range = y.split("-")
            start = int(my_range[0])
            end = int(my_range[1]) + 1
            # print(start, end)
            if int(i) in range(start, end):
                counter.append(i)
                # print(counter)
                # print(i)
    response = list(dict.fromkeys(counter))

    print(len(response))
    return len(response)


check_in_range(product_list, fresh_ranges)
