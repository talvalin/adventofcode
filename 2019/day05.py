import intcode_computer as IntcodeComputer

def load_intcode():
    with open('../aoc_inputs/2019/day05_input.txt') as input:
        return [int(x) for x in input.read().strip('\n').split(',')]

def main():
    # initialise Intcode computer
    intcode = load_intcode()
    part1_output = IntcodeComputer.IntcodeComputer(intcode, [1]).execute()
    part2_output = IntcodeComputer.IntcodeComputer(intcode, [5]).execute()
    
    print("Part 1 output: ", part1_output)
    print("Part 2 output: ", part2_output)

if __name__ == "__main__":
    main()