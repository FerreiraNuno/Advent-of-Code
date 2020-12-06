def import_data():
    with open("input(Day6).txt") as file:
        input_list = [line.rstrip() for line in file]
    item_combiner = []
    data = []
    for item in input_list:
        if item != "":
            item_combiner.append(item)
        else:
            data.append(item_combiner)
            item_combiner = []
    return data

data = import_data()

sum = 0
for group in data:
    overall_string = list(group[0])
    for person_responses in group:
        match_string = list(person_responses)
        new_string = []
        for letter in match_string:
            duplicate_responses = []
            if letter in overall_string:
                new_string.append(letter)
        overall_string = new_string
    sum += len(new_string)

print(sum)

