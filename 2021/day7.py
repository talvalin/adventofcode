import itertools

def load_input():
    with open('../aoc_inputs/2021/day07_input.txt') as input:
        return input.read().splitlines()

def part1(input):
    fuel_outcomes = []
    max_shift = input[-1] - input[0]
    for x in range(input[0], max_shift):
        # calculate fuel expenditure for each possible shift position 
        # and each crab's starting position
        fuel = 0
        for crab in input:
            fuel += abs(x-crab)
        fuel_outcomes.append(fuel)    
    return min(fuel_outcomes)

def part2(input):
    fuel_outcomes = []
    max_shift = input[-1] - input[0]
    for x in range(input[0], max_shift):
        # calculate fuel expenditure for each possible shift position 
        # and each crab's starting position
        fuel = 0
        for crab in input:
            fuel += sum(range(1, abs(x-crab)+1))
        fuel_outcomes.append(fuel)    
    return min(fuel_outcomes)

def main():
    input = sorted([int(x) for x in load_input()[0].split(',')])
    print(part1(input))
    print(part2(input))
        
if __name__ == "__main__":
    main()