def load_input():
    with open('../aoc_inputs/2021/day03_input.txt') as input:
        return input.read().splitlines()

def part1(diagnostics):
    diagnostics_size_check = len(diagnostics) // 2
    # create list of vertical slices through the diagnostics array
    verticals = [[y[x] for y in diagnostics] for x in range(len(diagnostics[0]))]

    # next loop through each element, sum the '1's and see if the total is greater than half the size of the diagnostics
    gamma_rate = ''
    for v in verticals:
        if sum(x[0]=='1' for x in v) > diagnostics_size_check:
             gamma_rate += '1'
        else:
            gamma_rate += '0'
    epsilon_rate = ''.join('1' if x == '0' else '0' for x in gamma_rate)
    gamma_rate_decimal = int(gamma_rate, 2)
    epsilon_rate_decimal = int(epsilon_rate, 2)

    print(gamma_rate_decimal*epsilon_rate_decimal)  

def part2(diagnostics):
    return 0
    
def main():
    diagnostics = load_input()
    part1(diagnostics)
    #part2(diagnostics)

if __name__ == "__main__":
    main()