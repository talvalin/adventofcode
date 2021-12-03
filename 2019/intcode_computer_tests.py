import unittest
import itertools
import intcode_computer as IntcodeComputer


class IntCode_Computer_Tests(unittest.TestCase):

    def setUp(self):
        self.intcode_computer = IntcodeComputer.IntcodeComputer(debug=False)

    def test_opcode(self):
        opcode = self.intcode_computer.process_opcode(1002)
        self.assertEqual(opcode[0], 2)

    def test_parameter_modes(self):
        opcode = self.intcode_computer.process_opcode(1002)
        self.assertEqual(opcode[1], [0, 1, 0])

    def test_program1(self):
        self.intcode_computer.intcode = [3,0,4,0,99]
        self.intcode_computer.input = [10249]
        self.assertEqual(self.intcode_computer.execute(), 10249)

    def test_opcode8_position_mode(self):
        self.intcode_computer.intcode = [3,9,8,9,10,9,4,9,99,-1,8]
        self.intcode_computer.input = [8]
        self.assertEqual(self.intcode_computer.execute(), 1)

    def test_opcode7_position_mode(self):
        self.intcode_computer.intcode = [3,9,7,9,10,9,4,9,99,-1,8]
        self.intcode_computer.input = [8]
        self.assertEqual(self.intcode_computer.execute(), 0)

    def test_opcode8_immediate_mode(self):
        self.intcode_computer.intcode = [3,3,1108,-1,8,3,4,3,99]
        self.intcode_computer.input = [8]
        self.assertEqual(self.intcode_computer.execute(), 1)

    def test_opcode7_immediate_mode(self):
        self.intcode_computer.intcode = [3,3,1107,-1,8,3,4,3,99]
        self.intcode_computer.input = [8]
        self.assertEqual(self.intcode_computer.execute(), 0)

    def test_jump_test_position_mode_zeroinput(self):
        self.intcode_computer.intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.intcode_computer.input = [0]
        self.assertEqual(self.intcode_computer.execute(), 0)

    def test_jump_test_position_mode_nonzeroinput(self):
        self.intcode_computer.intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.intcode_computer.input = [2]
        self.assertEqual(self.intcode_computer.execute(), 1)

    def test_jump_test_immediate_mode_zeroinput(self):
        self.intcode_computer.intcode = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        self.intcode_computer.input = [0]
        self.assertEqual(self.intcode_computer.execute(), 0)

    def test_jump_test_immediate_mode_nonzeroinput(self):
        self.intcode_computer.intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.intcode_computer.input = [3]
        self.assertEqual(self.intcode_computer.execute(), 1)

    def test_long_example_below8(self):
        self.intcode_computer.intcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        self.intcode_computer.input = [7]
        self.assertEqual(self.intcode_computer.execute(), 999)

    def test_long_example_equals8(self):
        self.intcode_computer.intcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        self.intcode_computer.input = [8]
        self.assertEqual(self.intcode_computer.execute(), 1000)

    def test_long_example_above8(self):
        self.intcode_computer.intcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        self.intcode_computer.input = [9]
        self.assertEqual(self.intcode_computer.execute(), 1001)

    def test_max_thruster_fixed_phase_settings(self):
        intcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        phase_settings = [4,3,2,1,0]
        input_output_value = 0
        
        for setting in phase_settings:
            # initialise amplifier with phase setting
            inputs = [setting, input_output_value]
            input_output_value = IntcodeComputer.IntcodeComputer(intcode, inputs).execute()
        self.assertEqual(input_output_value, 43210)

    def test_max_thruster_fixed_phase_settings2(self):
        intcode = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        phase_settings = [0,1,2,3,4]
        input_output_value = 0
        
        for setting in phase_settings:
            # initialise amplifier with phase setting
            inputs = [setting, input_output_value]
            input_output_value = IntcodeComputer.IntcodeComputer(intcode, inputs).execute()
        self.assertEqual(input_output_value, 54321)

    def test_max_thruster_permutations(self):
        intcode = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        phase_setting_permutations = itertools.permutations(range(5))
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

        self.assertEqual(max_thruster_signal, 65210)
        self.assertEqual(max_phase_settings, (1,0,4,3,2))

    def test_max_thruster_feedback_fixed_phase(self):
        intcode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        phase_settings = [[9],[8],[7],[6],[5]]
        input_output_value = 0
        max_thruster_signal = 0

        # initialise amplifiers
        amplifierA =  IntcodeComputer.IntcodeComputer(intcode, phase_settings[0])
        amplifierB =  IntcodeComputer.IntcodeComputer(intcode, phase_settings[1])
        amplifierC =  IntcodeComputer.IntcodeComputer(intcode, phase_settings[2])
        amplifierD =  IntcodeComputer.IntcodeComputer(intcode, phase_settings[3])
        amplifierE =  IntcodeComputer.IntcodeComputer(intcode, phase_settings[4])

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
                max_thruster_signal = input_output_value
                break

        self.assertEqual(max_thruster_signal, 139629729)

    def test_max_thruster_feedback_permutation(self):
        intcode = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
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

        self.assertEqual(max_thruster_signal, 18216)
        self.assertEqual(max_phase_settings, (9,7,8,5,6))

if __name__ == "__main__":
    unittest.main()