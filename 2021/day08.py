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
    # guess we do it properly this time lol
    segment_wire_mapping = {'a':0,
                            'b':0,
                            'c':0,
                            'd':0,
                            'e':0,
                            'f':0,
                            'gt':0
                            }
    return 0

def main():
    raw_input = load_input()
    input = []
    for line in raw_input:
        patterns = line.split('|')[0].rstrip().split()
        output = line.split('|')[1].lstrip().split()
        input.append((patterns, output))
    print(part1(input))
    #print(part2(input))
        
if __name__ == "__main__":
    main()