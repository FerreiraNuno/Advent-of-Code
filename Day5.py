from math import floor
from math import ceil


array = ["BBFFBBFLRL", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]

def import_data():
    with open("input(Day5).txt") as file:
        input_list = [line.rstrip() for line in file]
    return input_list


def part1(array):
    highest_id = 0
    for commands in array:
        # collumn
        upper = 7
        lower = 0
        for letter in commands[7:]:
            intermediary = lower + ((upper - lower) / 2)
            if letter == "L":
                upper = floor(intermediary)
            elif letter == "R":
                lower = ceil(intermediary)
        collumn = lower
        #row
        upper = 127
        lower = 0
        for letter in commands[:7]:
            intermediary = lower + ((upper - lower) / 2)
            if letter == "F":
                upper = floor(intermediary)
            elif letter == "B":
                lower = ceil(intermediary)
        row = lower
        seat_id = row * 8 + collumn
        if seat_id >= highest_id:
            highest_id = seat_id
    return highest_id

def part2(array):
    seat_ids = []
    for commands in array:
        # collumn
        upper = 7
        lower = 0
        for letter in commands[7:]:
            intermediary = lower + ((upper - lower) / 2)
            if letter == "L":
                upper = floor(intermediary)
            elif letter == "R":
                lower = ceil(intermediary)
        collumn = lower
        # row
        upper = 127
        lower = 0
        for letter in commands[:7]:
            intermediary = lower + ((upper - lower) / 2)
            if letter == "F":
                upper = floor(intermediary)
            elif letter == "B":
                lower = ceil(intermediary)
        row = lower
        seat_id = row * 8 + collumn
        seat_ids.append(seat_id)
    seat_ids.sort()
    previous_item = seat_ids[0] - 1
    print(seat_ids)
    for item in seat_ids:
        if item != previous_item + 1:
            return item - 1
        previous_item = item



array = import_data()
print(part2(array))
