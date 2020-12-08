def import_data():
    with open("input(Day7).txt") as file:
        input_list = [line.rstrip()[:-1] for line in file]
    rules = []
    for line in input_list:
        line = line.split(" contain ")
        outer_bag = line[0][:-5]
        contains = {}
        inner_bags = line[1].split(", ")
        for item in inner_bags:
            if item.endswith("s"):
                item = item[:-5]
            else:
                item = item[:-4]
            dic = {item[2:]: item[0]}
            contains.update(dic)
        if contains == "":
            rule = {outer_bag: 1}
        else:
            rule = {outer_bag: contains}
        rules.append(rule)
    return rules


rules = import_data()

def part1(searched_bag, rules):
    already_searched_bags = []
    def checkContainCount(searched_bag, rules, already_searched_bags):
        count = 0
        for rule in rules:
            for key, value in rule.items():
                for value in rule.get(key):
                    if value == searched_bag:
                        if not key in already_searched_bags:
                            count += 1
                            count += checkContainCount(key, rules, already_searched_bags)
        already_searched_bags.append(searched_bag)
        return count
    return checkContainCount(searched_bag, rules, already_searched_bags)



def part2(searched_bag, rules):
    already_searched_bags = []
    def checkContainCount(searched_bag, rules, already_searched_bags):
        count = 0
        for rule in rules:
            for key, value in rule.items():
                if key == searched_bag:
                    print(searched_bag + " rule: "+ str(value))
                    for key, value in value.items():
                        if value != "n":
                            print("value: " + str(value))
                            count += int(value) * int(checkContainCount(key, rules, already_searched_bags))
                            if int(checkContainCount(key, rules, already_searched_bags)) != 1:
                                count += int(value)
                        else:
                            return 1
        return count
    return checkContainCount(searched_bag, rules, already_searched_bags)


print(part2("shiny gold", rules))