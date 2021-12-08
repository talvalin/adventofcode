import itertools

def load_input():
    with open('../aoc_inputs/2021/day06_test_input.txt') as input:
        return input.read().splitlines()

def part1(input, days):
    for day in range(0, days):
        new_fish = 0
        for idx, fish in enumerate(input):
            if fish == 0:
                input[idx] = 6
                new_fish += 1
            else:
                input[idx] = fish-1
        input.extend([8 for i in range(new_fish)])      
    return len(input)

def part2():
    pass

def main():
    input = [int(x) for x in load_input()[0].split(',')]
    print(part1(input, 256))
    

if __name__ == "__main__":
    main()