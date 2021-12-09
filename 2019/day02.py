def run_intcode(int_code):
    opcode = 0
    instruction_pointer = 0
    while True:
        opcode = int_code[instruction_pointer]
        if opcode == 99:
            break
        else:
            # get parameters
            parameter1, parameter2, parameter3 = int_code[instruction_pointer+1:instruction_pointer+4]

            if opcode == 1:
                # do addition
                int_code[parameter3] = int_code[parameter1] + int_code[parameter2]
            elif opcode == 2:
                # do multiplication
                int_code[parameter3] = int_code[parameter1] * int_code[parameter2]
        instruction_pointer += 4

    return int_code

def run_gravity_assist(noun, verb):
    with open('../aoc_inputs/2019/day02_input.txt') as input:
        int_code = []
        for line in input:
            int_code = list(map(int, line.split(','))) 
        int_code[1] = noun
        int_code[2] = verb
        return(run_intcode(int_code)[0])

def main():
    # part 1
    print(run_gravity_assist(12, 2))

    # part 2
    output = 0
    for noun in range(99):
        for verb in range(99):
            output = run_gravity_assist(noun, verb)
            if output == 19690720:
                print((100 * noun) + verb)
                break

if __name__ == "__main__":
    main()