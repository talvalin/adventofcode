# aoc202113.py

import pathlib
import sys
from collections import Counter

def create_pairs(polymer):
    return [x+y for x,y in zip(polymer[0:], polymer[1:])]

def create_pair_insertion_rules(rules):
    rules_dict = {}
    for rule in rules.split('\n'):
        pair, element = rule.split(" -> ")
        rules_dict[pair] = element
    return rules_dict

def parse(puzzle_input):
    """Parse input"""
    polymer, rules_s = puzzle_input.split('\n\n')
    rules = create_pair_insertion_rules(rules_s)

    return (polymer, rules)  

def part1(data, steps):
    """Solve part 1"""
    # brute force solution
    polymer = data[0]
    rules = data[1]

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

def part2(data, steps):
    """Solve part 2"""
    # instead of doing direct string updates, use a Counter to keep track
    polymer = data[0]
    rules = data[1]

    # set up the Counter object
    pair_counts = Counter()

    # initialise the Counter object with the initial polymer
    for i in range(len(polymer)-1):
        pair_counts[polymer[i:i+2]] += 1

    # loop over the specified number of steps and add two new pairs
    # for each insertion rule
    # Eg: if HH->N, then by adding N in between to make HNH, we can
    # say that we actually have HN and NH now
    for _ in range(steps):
        new_pair_counts = Counter()
        char_counts = Counter()
        for k,v in pair_counts.items():
            new_pair_counts[ k[0] + rules[k]  ] += v
            new_pair_counts[ rules[k] + k[1]  ] += v
        pair_counts = new_pair_counts

    # sum the individual elements
    count_individual = Counter()

    # by summing up all of the halves of each pair means we are double counting
    # however, we've also missed off adding the very last "letter" in the starting polymer
    # so we need to add one to the final count and then divide by 2
    for k,v in pair_counts.items():
        count_individual[k[0]] += v
        count_individual[k[1]] += v

    sorted_counts = count_individual.most_common()

    return (sorted_counts[0][1] - sorted_counts[-1][1] + 1) // 2

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data, 10)
    solution2 = part2(data, 40)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))