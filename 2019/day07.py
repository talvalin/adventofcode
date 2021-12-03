import itertools
import intcode_computer as IntcodeComputer

def load_intcode():
    with open('./day07_input.txt') as input:
        return [int(x) for x in input.read().strip('\n').split(',')]

def get_phase_setting_permutations(start, end):
    return itertools.permutations(range(start, end))

def part1():
    # initialise Intcode computer
    intcode = load_intcode()
    phase_setting_permutations = get_phase_setting_permutations(0,5)
    max_thruster_signal = 0
    max_phase_settings = []

    for phase_settings in phase_setting_permutations:
        input_output_value = 0
        for setting in phase_settings:
            # initialise amplifier with phase setting
            inputs = [setting, input_output_value]
            input_output_value = IntcodeComputer.IntcodeComputer(intcode, inputs).execute()
        if input_output_value > max_thruster_signal:
            max_thruster_signal = input_output_value
            max_phase_settings = phase_settings

    print("Max thruster signal: ", max_thruster_signal)
    print("Max phase settings: ", max_phase_settings)

def part2():
    # initialise Intcode computer
    intcode = load_intcode()
    phase_setting_permutations = itertools.permutations(range(5,10))
    max_thruster_signal = 0
    max_phase_settings = []

    for phase_settings in phase_setting_permutations:
        # initialise amplifiers
        amplifierA =  IntcodeComputer.IntcodeComputer(intcode, [phase_settings[0]])
        amplifierB =  IntcodeComputer.IntcodeComputer(intcode, [phase_settings[1]])
        amplifierC =  IntcodeComputer.IntcodeComputer(intcode, [phase_settings[2]])
        amplifierD =  IntcodeComputer.IntcodeComputer(intcode, [phase_settings[3]])
        amplifierE =  IntcodeComputer.IntcodeComputer(intcode, [phase_settings[4]])
        input_output_value = 0

        while True:
            # reset all amplifier statuses
            amplifierA.status = 'WORKING'
            amplifierB.status = 'WORKING'
            amplifierC.status = 'WORKING'
            amplifierD.status = 'WORKING'
            amplifierE.status = 'WORKING'

            amplifierA.add_input(input_output_value)
            input_output_value =  amplifierA.execute()
            amplifierB.add_input(input_output_value)
            input_output_value =  amplifierB.execute()
            amplifierC.add_input(input_output_value)
            input_output_value =  amplifierC.execute()
            amplifierD.add_input(input_output_value)
            input_output_value =  amplifierD.execute()
            amplifierE.add_input(input_output_value)
            input_output_value =  amplifierE.execute()

            if amplifierE.status == 'HALTED':
                if input_output_value > max_thruster_signal:
                    max_thruster_signal = input_output_value
                    max_phase_settings = phase_settings
                break
    print("Max thruster signal: ", max_thruster_signal)
    print("Max phase settings: ", max_phase_settings)

if __name__ == "__main__":
    part1()
    part2()