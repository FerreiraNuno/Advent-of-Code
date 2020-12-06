def import_data():
    with open("input(Day6).txt") as file:
        input_list = [line.rstrip() for line in file]
    item_combiner = ""
    data = []
    for item in input_list:
        if item != "":
            item_combiner += item
        else:
            data.append(item_combiner)
            item_combiner = ""
    return data


data = import_data()

sum = 0
for group in data:
    #remove duplicates
    group = list(dict.fromkeys(list(group)))
    sum += len(group)
print(sum)

