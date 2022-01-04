import copy

def load_input():
    with open('../aoc_inputs/2021/day06_test_input.txt') as input:
        return input.read().splitlines()

def part1(input, days):
    fish_school = copy.deepcopy(input)
    for day in range(0, days):
        new_fish = 0
        for idx, fish in enumerate(fish_school):
            if fish == 0:
                fish_school[idx] = 6
                new_fish += 1
            else:
                fish_school[idx] = fish-1
        fish_school.extend([8 for i in range(new_fish)])      
    return len(fish_school)

def part2(input, days):
    # create fish school
    fish_school = [0] * 9
    
    # initial update of school
    for x in input:
        fish_school[x] += 1

    previous_day_new_fish = 0    
    for day in range(0, days):
        # rotate array
        for i in range(8):
            fish_school[i] = fish_school[i+1]
        fish_school[8] = 0

        # add fish in the zero index to the 6th index and the 8th index
        if previous_day_new_fish:   
            fish_school[6] += previous_day_new_fish
            fish_school[8] = previous_day_new_fish
        previous_day_new_fish = fish_school[0]

    return sum(x for x in fish_school)

def main():
    input = [int(x) for x in load_input()[0].split(',')]
    print(part1(input, 80))
    print(part2(input, 256))
    
if __name__ == "__main__":
    main()