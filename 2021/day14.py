from collections import Counter

def load_input():
    with open('../aoc_inputs/2021/day14_test_input.txt') as input:
        return input.read().splitlines()

def create_pairs(polymer):
    return [x+y for x,y in zip(polymer[0:], polymer[1:])]

def create_pair_insertion_rules(rules):
    rules_dict = {}
    for rule in rules:
        pair, element = rule.split(" -> ")
        rules_dict[pair] = element
    return rules_dict

def part1(raw_input, steps):
    polymer = raw_input[0]
    rules = create_pair_insertion_rules(raw_input[2:])
    
    for step in range(steps):
        new_polymer = ""
        pairs = create_pairs(polymer)
        # for each pair, check for the insertion rule and append
        # assumption is that all pairs have a valid insertion rule
        for pair in pairs:
            new_polymer += pair[0] + rules[pair]
        # add the second part of the final pair to the string
        new_polymer += pairs[-1][1] 
        polymer = new_polymer
    element_frequencies = Counter(polymer).most_common()
    return element_frequencies[0][1] - element_frequencies[-1][1]

def part2(input, steps):
    return 0

def main():
    raw_input = load_input()
    print(part1(raw_input, 10))
    print(part2(raw_input, 40))
        
if __name__ == "__main__":
    main()