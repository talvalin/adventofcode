def load_input():
    with open('../aoc_inputs/2021/day03_input.txt') as input:
        return input.read().splitlines()

def binary_conversion(seq):
    return int(''.join([str(x) for x in seq]), 2)

def most_common_bits(input):
    result = []
    for i,x in enumerate(input):
       result.append('1' if x.count('1') >= x.count('0') else '0')
    return result

def least_common_bits(input):
    result = []
    for i,x in enumerate(input):
       result.append('1' if x.count('1') < x.count('0') else '0')
    return result

def part1(diagnostics):
    # create list of vertical slices through the diagnostics array
    verticals = [[y[x] for y in diagnostics] for x in range(len(diagnostics[0]))]

    # enumerate each element and compare the sum of '1's and '0's
    gamma_rate = most_common_bits(verticals)
    epsilon_rate = least_common_bits(verticals)
    print(gamma_rate)
    print(epsilon_rate)
    gamma_rate_decimal = binary_conversion(gamma_rate)
    epsilon_rate_decimal = binary_conversion(epsilon_rate)

    print(gamma_rate_decimal*epsilon_rate_decimal)  

def calculate_oxygen_rate(diagnostics):
    for idx in range(len(diagnostics[0])):
        # create list of vertical slices through the diagnostics array
        verticals = [[y[x] for y in diagnostics] for x in range(len(diagnostics[0]))]
        most = most_common_bits(verticals)
        filtered = [candidate for candidate in diagnostics if candidate[idx] == most[idx]]
        if len(filtered) == 0:
            raise Exception("Fail - filtered list is empty!")
        elif len(filtered) == 1:
            return filtered.pop()
        diagnostics = filtered

def calculate_co2_rating(diagnostics):
    for idx in range(len(diagnostics[0])):
        # create list of vertical slices through the diagnostics array
        verticals = [[y[x] for y in diagnostics] for x in range(len(diagnostics[0]))]
        least = least_common_bits(verticals)
        filtered = [candidate for candidate in diagnostics if candidate[idx] == least[idx]]
        if len(filtered) == 0:
            raise Exception("Fail - filtered list is empty!")
        elif len(filtered) == 1:
            return filtered.pop()
        diagnostics = filtered

def part2(diagnostics):
    oxy = calculate_oxygen_rate(diagnostics)
    co2 = calculate_co2_rating(diagnostics)
    oxy_decimal = binary_conversion(oxy)
    co2_decimal = binary_conversion(co2)
    print(oxy_decimal * co2_decimal)

def main():
    diagnostics = load_input()
    part1(diagnostics)
    part2(diagnostics)

if __name__ == "__main__":
    main()