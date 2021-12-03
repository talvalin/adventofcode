from heapq import nsmallest

def load_input():
    with open('./2015/inputs/day02_input.txt') as input:
        output = []
        for line in input.readlines():
            dimensions = line.split('x')
            dimension_tuple = (int(dimensions[0]), int(dimensions[1]), int(dimensions[2]))
            output.append(dimension_tuple)
        return output

def part1(present_list):
    initial_calc = [(x*y, x*z, y*z) for x,y,z in present_list]
    final_calc = sum(min(calc) + sum(calc) * 2 for calc in initial_calc)
    print(final_calc)

def part2(present_list):
    initial_calc = [
        present[0] * present[1] * present[2] + 
        (nsmallest(3, present)[0] + nsmallest(3, present)[1]) * 2 
        for present in present_list
    ]
    print(sum(initial_calc))

def main():
    present_list = load_input()
    part1(present_list)
    part2(present_list)

if __name__ == "__main__":
    main()