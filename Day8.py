
with open("input(Day8).txt") as file:
    input_list = [line.rstrip() for line in file]

y = 0
commands_list = []
for item in input_list:
    commands_list.append({item: y})




def part1():
    i = 0
    accumulator = 0
    while i < len(commands_list):
        print(commands_list[i])
        for key, value in commands_list[i].items():
            if value != 0:
                return accumulator
            else:
                commands_list[i].update({key: value + 1})
                split_key = key.split()
                operation = split_key[0]
                argument = split_key[1]
                # ab hier hat man nur die operation und den argument
                if operation == "nop":
                    i += 1
                elif operation == "acc":
                    accumulator += int(argument)
                    i += 1
                elif operation == "jmp":
                    i += int(argument)
                else:
                    print("invalid argument")
                    break
        if i == len(commands_list) - 1:
            break


def part2():
    i = 0
    accumulator = 0
    previous_item = {}
    while i < len(commands_list):
        print(commands_list[i])
        for key, value in commands_list[i].items():
            if value != 0:
                for a, b in previous_item.items():
                    previous_item.pop(a)
                    previous_item.update({"nop": 0})
                    i = previous_index
            else:
                commands_list[i].update({key: value + 1})
                split_key = key.split()
                operation = split_key[0]
                argument = split_key[1]
                # ab hier hat man nur die operation und den argument
                if operation == "nop":
                    previous_item = commands_list[i]
                    previous_index = i
                    i += 1
                elif operation == "acc":
                    accumulator += int(argument)
                    previous_item = commands_list[i]
                    previous_index = i
                    i += 1
                elif operation == "jmp":
                    previous_item = commands_list[i]
                    previous_index = i
                    i += int(argument)
                else:
                    print("invalid argument")
                    break
        if i == len(commands_list) - 1:
            return accumulator


print(part2())
