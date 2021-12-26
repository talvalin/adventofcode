def load_input():
    with open('../aoc_inputs/2021/day08_input.txt') as input:
        return input.read().splitlines()

def part1(input):
    # Just count the number of output values with a length of 2,3,4 or 7
    total = 0
    for item in input:
        total += sum(1 for x in item[1] if len(x) in [2,3,4,7])
    return total

def part2(input):
    output = 0

    for line in input:
        segment_wire_mapping = {'a':0,
                                'b':0,
                                'c':0,
                                'd':0,
                                'e':0,
                                'f':0,
                                'g':0
                                }

        number_pattern_mapping = {'0':'',
                                  '1':'',
                                  '2':'',
                                  '3':'',
                                  '4':'',
                                  '5':'',
                                  '6':'',
                                  '7':'',
                                  '8':'',
                                  '9':'',}
        
        pattern_dict = {'2':[],
                        '3':[],
                        '4':[],
                        '5':[],
                        '6':[],
                        '7':[]}

        for pattern in line[0]:
            length = str(len(pattern))
            pattern_dict[length].append(set(pattern))

        # set the numbers that have a unique pattern length
        # 1
        number_pattern_mapping['1'] = ''.join(sorted(list(pattern_dict['2'][0])))

        # 4
        number_pattern_mapping['4'] = ''.join(sorted(list(pattern_dict['4'][0])))

        # 7
        number_pattern_mapping['7'] = ''.join(sorted(list(pattern_dict['3'][0])))

        # 8
        number_pattern_mapping['8'] = ''.join(sorted(list(pattern_dict['7'][0])))

        # get a
        segment_wire_mapping['a'] = pattern_dict['3'][0].difference(pattern_dict['2'][0])
        
        for number in pattern_dict['6']:
            # get c
            if not pattern_dict['7'][0].difference(number, pattern_dict['2'][0]):
                # 6
                segment_wire_mapping['c'] = pattern_dict['7'][0].difference(number)
                number_pattern_mapping['6'] = ''.join(sorted(list(number)))
            else:
                # get g
                if not pattern_dict['4'][0].difference(number):
                    # 9
                    segment_wire_mapping['g'] = number.difference(pattern_dict['4'][0], pattern_dict['3'][0])
                    number_pattern_mapping['9'] = ''.join(sorted(list(number)))
                else:
                    # get d and b
                    # 0
                    segment_wire_mapping['d'] = pattern_dict['7'][0].difference(number)
                    segment_wire_mapping['b'] = pattern_dict['4'][0].difference(pattern_dict['2'][0], segment_wire_mapping['d'])
                    number_pattern_mapping['0'] = ''.join(sorted(list(number)))
        # get f
        segment_wire_mapping['f'] = pattern_dict['2'][0].difference(segment_wire_mapping['c'])

        # get e
        all_segments_but_e = segment_wire_mapping['a'].union(segment_wire_mapping['b'], 
                                                            segment_wire_mapping['c'],
                                                            segment_wire_mapping['d'],
                                                            segment_wire_mapping['f'],
                                                            segment_wire_mapping['g'])
        segment_wire_mapping['e'] = set('abcdefg').difference(all_segments_but_e)

        # create 2, 3, 5 based on knowing the wire/segment mappings
        # 2 = acdeg, 3 = acdfg, 5 = abdfg
        two = segment_wire_mapping['a'].union(segment_wire_mapping['c'],
                                              segment_wire_mapping['d'],
                                              segment_wire_mapping['e'],
                                              segment_wire_mapping['g'])
        three = segment_wire_mapping['a'].union(segment_wire_mapping['c'],
                                                segment_wire_mapping['d'],
                                                segment_wire_mapping['f'],
                                                segment_wire_mapping['g'])
        five = segment_wire_mapping['a'].union(segment_wire_mapping['b'],
                                               segment_wire_mapping['d'],
                                               segment_wire_mapping['f'],
                                               segment_wire_mapping['g'])
        number_pattern_mapping['2'] = ''.join(sorted(list(two)))
        number_pattern_mapping['3'] = ''.join(sorted(list(three)))
        number_pattern_mapping['5'] = ''.join(sorted(list(five)))

        output_str = ''
        for pattern in line[1]:
            for k,v in number_pattern_mapping.items():
                if v == ''.join(sorted(pattern)):
                    output_str += k
        output += int(output_str)
    return output

def main():
    raw_input = load_input()
    input = []
    for line in raw_input:
        patterns = line.split('|')[0].rstrip().split()
        output = line.split('|')[1].lstrip().split()
        input.append((patterns, output))
    print(part1(input))
    print(part2(input))
        
if __name__ == "__main__":
    main()