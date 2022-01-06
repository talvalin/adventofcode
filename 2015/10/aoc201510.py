# aoc202113.py

import pathlib
import sys
from itertools import groupby

def parse(puzzle_input):
    """Parse input"""
    return puzzle_input

def part1(data, steps):
    """Solve part 1"""
    for step in range(steps):
        groups = [list(g) for k,g in groupby(data)]
        new_string = ''.join([str(len(x))+x[0] for x in groups])
        data = new_string
    
    return len(data)

def part2(data, steps):
    """Solve part 2"""
    return part1(data, steps)

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data, 40)
    solution2 = part2(data, 50)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))