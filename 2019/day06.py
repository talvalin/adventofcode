def load_input():
    with open('../aoc_inputs/2019/day06_test_input.txt') as input:
        return input.read().splitlines()

def part1(planets):
    pass

def part2():
    pass

def main():
    input = load_input()
    planets = []
    for line in input:
        planets.append(line.split(')'))
    print(planets)
    print(part1(planets))
        
if __name__ == "__main__":
    main()