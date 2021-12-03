def load_input():
    with open('./inputs/day02_input.txt') as input:
        return input.read().splitlines()

def part1(commands):
    forward = 0
    depth = 0
    for command in commands:
        direction, value = command.split()
        int_v = int(value)
        if direction == 'forward':
            forward += int_v
        if direction == 'down':
            depth += int_v
        elif direction == 'up':
            depth -= int_v    
    print(forward * depth)    

def part2(commands):
    forward = 0
    depth = 0
    aim = 0
    for command in commands:
        direction, value = command.split()
        int_v = int(value)
        if direction == 'forward':
            forward += int_v
            depth += int_v * aim
        if direction == 'down':
            aim += int_v
        elif direction == 'up':
            aim -= int_v
    print(forward * depth)    
    
def main():
    commands = load_input()
    part1(commands)
    part2(commands)

if __name__ == "__main__":
    main()