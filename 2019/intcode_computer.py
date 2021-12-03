import copy

status_flags = ['WORKING', 'HALTED', 'WAITING', 'ERROR']

class IntcodeComputer:
    def __init__(self, intcode=None, input=None, pointer=0, debug=False):
        self.intcode = copy.deepcopy(intcode)
        self.input = input
        self.pointer = pointer
        self.debug = debug
        self.last_output = None
        self.status = status_flags[0]

        self.dispatch_map = {
            1: self.AddInstruction,
            2: self.MultiplyInstruction,
            3: self.InputInstruction,
            4: self.OutputInstruction,
            5: self.JumpIfTrueInstruction,
            6: self.JumpIfFalseInstruction,
            7: self.LessThanInstruction,
            8: self.EqualsInstruction,
            99: self.HaltInstruction
        }

        self.current_opcode = None
    
    def add_input(self, value):
        self.input.append(value)

    def get_next_input(self):
        if self.input:
            return self.input.pop(0)
        else:
            return None

    def get_parameter_value(self, parameter, mode):
        value = 0
        if mode == 0:
            value = self.intcode[parameter]
        elif mode == 1:
            value = parameter
        return value

    def process_opcode(self, opcode):
        # pad opcode
        opcode_array = list(str(opcode))
        if len(opcode_array) < 5:
            for _ in range(5-len(opcode_array)):
                opcode_array.insert(0, "0")

        processed_opcode = []
        processed_opcode.append(int(opcode_array[-2] + opcode_array[-1]))

        # create reversed list of parameter modes
        parameter_modes = [int(x) for x in reversed(opcode_array[0:3])]   

        # append parameters in reverse order
        processed_opcode.append(parameter_modes)
        return processed_opcode

    def execute(self):
        while self.status == 'WORKING':
            # get opcode
            self.current_opcode = self.process_opcode(self.intcode[self.pointer])
            self.dispatch_map[self.current_opcode[0]]()
            
        if self.status in ('HALTED', 'WAITING'):
            # print("Current instruction pointer: ", self.pointer)
            return self.last_output

    def AddInstruction(self):
        parameter1, parameter2, parameter3 = self.intcode[self.pointer+1:self.pointer+4]
        parameter1_value = self.get_parameter_value(parameter1, self.current_opcode[1][0])
        parameter2_value = self.get_parameter_value(parameter2, self.current_opcode[1][1])
        self.intcode[parameter3] = parameter1_value + parameter2_value
        self.pointer += 4

    def MultiplyInstruction(self):
        parameter1, parameter2, parameter3 = self.intcode[self.pointer+1:self.pointer+4]
        parameter1_value = self.get_parameter_value(parameter1, self.current_opcode[1][0])
        parameter2_value = self.get_parameter_value(parameter2, self.current_opcode[1][1])
        self.intcode[parameter3] = parameter1_value * parameter2_value
        self.pointer += 4

    def InputInstruction(self):
        # get parameter
        parameter = self.intcode[self.pointer+1]
        next_input = self.get_next_input()
        if next_input is None:
            # set status to waiting and do not advance pointer!
            self.status = status_flags[2]
        else:
            # we have input, so set parameter and advance pointer
            self.intcode[parameter] = next_input
            self.pointer += 2

    def OutputInstruction(self):
        parameter1 = self.intcode[self.pointer+1]
        parameter1_value = self.get_parameter_value(parameter1, self.current_opcode[1][0])
        self.last_output = parameter1_value
        self.pointer += 2

    def JumpIfTrueInstruction(self):
        parameter1, parameter2 = self.intcode[self.pointer+1:self.pointer+3]
        parameter1_value = self.get_parameter_value(parameter1, self.current_opcode[1][0])
        parameter2_value = self.get_parameter_value(parameter2, self.current_opcode[1][1])
        if parameter1_value != 0:
            self.pointer = parameter2_value
        else:
            self.pointer += 3

    def JumpIfFalseInstruction(self):
        parameter1, parameter2 = self.intcode[self.pointer+1:self.pointer+3]
        parameter1_value = self.get_parameter_value(parameter1, self.current_opcode[1][0])
        parameter2_value = self.get_parameter_value(parameter2, self.current_opcode[1][1])
        if parameter1_value == 0:
            self.pointer = parameter2_value
        else:
            self.pointer += 3

    def LessThanInstruction(self):
        parameter1, parameter2, parameter3 = self.intcode[self.pointer+1:self.pointer+4]
        parameter1_value = self.get_parameter_value(parameter1, self.current_opcode[1][0])
        parameter2_value = self.get_parameter_value(parameter2, self.current_opcode[1][1])
        self.intcode[parameter3] = 1 if parameter1_value < parameter2_value else 0
        self.pointer += 4

    def EqualsInstruction(self):
        parameter1, parameter2, parameter3 = self.intcode[self.pointer+1:self.pointer+4]
        parameter1_value = self.get_parameter_value(parameter1, self.current_opcode[1][0])
        parameter2_value = self.get_parameter_value(parameter2, self.current_opcode[1][1])
        self.intcode[parameter3] = 1 if parameter1_value == parameter2_value else 0
        self.pointer += 4

    def HaltInstruction(self):
        self.status = status_flags[1]