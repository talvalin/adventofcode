def load_input():
    with open('../aoc_inputs/2021/day02_input.txt') as input:
        return input.read().splitlines()

def part1(commands):
    forward = 0
    depth = 0
    for c in commands:
        command, units = c.split()
        value = int(units)
        match command: 
            case 'forward':
                forward += value
            case 'down':
                depth += value
            case 'up':
                depth -= value    
    print(forward * depth)    

def part2(commands):
    forward = 0
    depth = 0
    aim = 0
    for c in commands:
        command, units = c.split()
        value = int(units)
        match command: 
            case 'forward':
                forward += value
                depth += value * aim
            case 'down':
                aim += value
            case 'up':
                aim -= value    
    print(forward * depth)    
    
def main():
    commands = load_input()
    part1(commands)
    part2(commands)

if __name__ == "__main__":
    main()