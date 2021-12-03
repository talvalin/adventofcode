def load_input():
    with open('../aoc_inputs/2021/day03_input.txt') as input:
        return input.read().splitlines()

def part1(diagnostics):
    # create list of vertical slices through the diagnostics array
    verticals = [[y[x] for y in diagnostics] for x in range(len(diagnostics[0]))]

    # enumerate each element and compare the sum of '1's and '0's
    gamma_rate, epsilon_rate = [], []
    for i,x in enumerate(verticals):
        bit_check = 1 if x.count('1') > x.count('0') else 0
        gamma_rate.append(bit_check)
        epsilon_rate.append(int(not(bit_check)))
    gamma_rate_decimal = int(''.join([str(x) for x in gamma_rate]), 2)
    epsilon_rate_decimal = int(''.join([str(x) for x in epsilon_rate]), 2)

    print(gamma_rate_decimal*epsilon_rate_decimal)  

def part2(diagnostics):
    return 0

def main():
    diagnostics = load_input()
    part1(diagnostics)
    part2(diagnostics)

if __name__ == "__main__":
    main()