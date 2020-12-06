def import_data():
    with open("input(Day4).txt") as file:
        input_list = [line.rstrip() for line in file]
    item_combiner = ""
    data = []
    for item in input_list:
        if item != "":
            item_combiner += item + " "
        else:
            item_combiner = item_combiner[:-1]
            data.append(item_combiner)
            item_combiner = ""
    output = []
    # iterates through every person once
    for item in data:
        # creates dictionary for one person
        dic = {}
        person_list = item.split(" ")
        for i in person_list:
            data_point = i.split(":")
            dic.update({data_point[0]: data_point[1]})
        output.append(dic)
    return output

data = import_data()

def part1():
    conditions =["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    counter = 0
    for item in data:
        is_valid = True
        for condition in conditions:
            if item.get(condition) == None:
                is_valid = False
        if is_valid:
            counter += 1
    return counter

def part2():
    #check if passport is valid
    counter = 0
    conditions = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in data:
        keys_valid = True
        for condition in conditions:
            if passport.get(condition) == None:
                keys_valid = False
        #check for valid values
        values_valid = True
        if keys_valid:
            if not 1920 <= int(passport.get("byr")) <= 2002:
                values_valid = False
            if not 2010 <= int(passport.get("iyr")) <= 2020:
                values_valid = False
            if not 2020 <= int(passport.get("eyr")) <= 2030:
                values_valid = False
            if not (passport.get("hgt").endswith("in") or passport.get("hgt").endswith("cm")):
                values_valid = False
            elif passport.get("hgt").endswith("in"):
                if not 59 <= int(passport.get("hgt")[:-2]) <= 76:
                    values_valid = False
            elif passport.get("hgt").endswith("cm"):
                if not 150 <= int(passport.get("hgt")[:-2]) <= 193:
                    values_valid = False
            if not passport.get("hcl").startswith("#"):
                values_valid = False
            else:
                allowed_characters = ["#", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
                if not len(passport.get("hcl")) == 7:
                    values_valid = False
                else:
                    for letter in passport.get("hcl"):
                        if not letter in allowed_characters:
                            values_valid = False
            allowed_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if not passport.get("ecl") in allowed_eye_colors:
                values_valid = False

            if not (len(passport.get("pid")) == 9 and passport.get("pid").isdigit()):
                values_valid = False

        if keys_valid and values_valid:
            counter += 1
    return counter


print(part1())
print(part2())
