from collections import Counter
from os import close

def load_input():
    with open('../aoc_inputs/2021/day10_input.txt') as input:
        return input.read().splitlines()

chunk_pairs = {'(': ')',
               '[': ']',
               '{': '}',
               '<': '>'
               }

def check_syntax(line):
    chars = []
    for idx, c in enumerate(line):
        if c in '([{<':
            chars.append(c)
        else:
            if c != chunk_pairs[chars[-1]]:
                match c:
                    case ')':
                        return 3
                    case ']':
                        return 57
                    case '}':
                        return 1197
                    case '>':
                        return 25137
            else:
                chars.pop()
    return 0

def autocorrect(line):
    chars = []
    for idx, c in enumerate(line):
        if c in '([{<':
            chars.append(c)
        else:
            if c != chunk_pairs[chars[-1]]:
                # corrupted line, so ignore
                return 0
            else:    
                chars.pop()
    # by the end of the loop, we should have a list of open braces
    # step through in reverse order, determine the correct closing brace and then update the score
    line_total = 0
    for c in chars[::-1]:
        close_char = chunk_pairs[c]
        match close_char:
            case ')':
                line_total = line_total*5 + 1
            case ']':
                line_total = line_total*5 + 2
            case '}':
                line_total = line_total*5 + 3
            case '>':
                line_total = line_total*5 + 4
    return line_total

def part1(input):
    total = 0
    for line in input:
        total += check_syntax(line)
    return total

def part2(input):
    totals = []
    for line in input:
        score = autocorrect(line)
        if score:
            totals.append(score)
    totals.sort()
    middle_index = (len(totals) - 1) // 2
    return totals[middle_index]

def main():
    input = load_input()
    print(part1(input))
    print(part2(input))
        
if __name__ == "__main__":
    main()