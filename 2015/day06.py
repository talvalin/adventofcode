import re

def load_input():
    with open('./2015/inputs/day06_input.txt') as input:
        return input.readlines()

def part1(instructions, lights, regex):
    for line in instructions:
        instruction, x1, y1, x2, y2 = regex.split(line)[1:6]
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if instruction == 'turn on':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = 1
        elif instruction == 'turn off':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = 0
        elif instruction == 'toggle':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] = 0 if lights[x][y] == 1 else 1

    lights_on = sum(y for x in lights for y in x)
    print("Part 1: ", lights_on)
        

def part2(instructions, lights, regex):
    for line in instructions:
        instruction, x1, y1, x2, y2 = regex.split(line)[1:6]
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if instruction == 'turn on':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] += 1
        elif instruction == 'turn off':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if lights[x][y] == 0:
                        continue
                    else: 
                        lights[x][y] -= 1
        elif instruction == 'toggle':
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    lights[x][y] += 2

    lights_on = sum(y for x in lights for y in x)
    print("Part 2: ", lights_on)

def main():
    instructions = load_input()
    lights = [[0] * 1000 for x in range(1000)]
    
    # regular expression time
    pattern = r'^(turn off|turn on|toggle) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})'
    prog = re.compile(pattern)
    
    moar_lights = [[0] * 1000 for x in range(1000)]
    part1(instructions, lights, prog)
    part2(instructions, moar_lights, prog)


if __name__ == "__main__":
    main()