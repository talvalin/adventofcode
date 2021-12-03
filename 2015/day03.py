def load_input():
    with open('./2015/inputs/day03_input.txt') as input:
        return input.readline()

def part1(directions):
    current_x = 0
    current_y = 0
    position_list = []
    position_list.append((current_x, current_y))

    for direction in directions:
        if direction == '^':
            current_y += 1
        elif direction == 'v':
            current_y -= 1
        elif direction == '>':
            current_x += 1
        elif direction == '<':
            current_x -= 1
        position_list.append((current_x, current_y))

    print("Part 1: ", len(set(position_list)))

def part2(directions):
    # get all of Santa's visited locations
    current_x = 0
    current_y = 0
    santa_position_list = []
    santa_position_list.append((current_x, current_y))

    for direction in directions[::2]:
        if direction == '^':
            current_y += 1
        elif direction == 'v':
            current_y -= 1
        elif direction == '>':
            current_x += 1
        elif direction == '<':
            current_x -= 1
        santa_position_list.append((current_x, current_y))

    # get all of Robo-Santa's visited locations
    current_x = 0
    current_y = 0
    robosanta_position_list = []
    robosanta_position_list.append((current_x, current_y))
    for direction in directions[1::2]:
        if direction == '^':
            current_y += 1
        elif direction == 'v':
            current_y -= 1
        elif direction == '>':
            current_x += 1
        elif direction == '<':
            current_x -= 1
        robosanta_position_list.append((current_x, current_y))

    location_set = set(santa_position_list + robosanta_position_list)
    print("Part 2: ", len(location_set))

def main():
    directions = load_input()
    part1(directions)
    part2(directions)

if __name__ == "__main__":
    main()
