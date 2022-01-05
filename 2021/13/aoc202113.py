# aoc202113.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    points_s, instructions = puzzle_input.split('\n\n')
    points = set()
    for line in points_s.splitlines():
        x_s, y_s = line.split(',')
        points.add((int(x_s), int(y_s)))
    
    instructions_l = []
    for instruction in instructions.splitlines():
        instruction_s, n_s = instruction.split('=')
        axis = instruction_s[-1]
        n = int(n_s)
        instructions_l.append((axis,n))

    return (points, instructions_l)

def fold_paper(points, instruction): 
    axis, fold_line = instruction

    if axis == 'y':
        # for points with a y value lower than the fold value, just add to the new points set
        # for points with a y value greater than the fold value, determine their new y value 
        # then add to the new points set
        new_points = set()
        for point in points:
            if point[1] > fold_line:
                new_y = 2*fold_line - point[1]
                new_points.add((point[0],new_y))
            else:
                new_points.add(point)
        points = new_points        
    elif axis == 'x':
        # for points with a x value lower than the fold value, just add to the new points set
        # for points with a x value greater than the fold value, determine their new x value 
        # then add to the new points set
        new_points = set()
        for point in points:
            if point[0] > fold_line:
                new_x = 2*fold_line - point[0]
                new_points.add((new_x, point[1]))
            else:
                new_points.add(point)
        points = new_points
    
    return points

def print_points(points):
    """Print the points for part 2"""
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x,y) in points:
                print('#', end='')
            else:
                print(' ', end='')
        print()            

def part1(data):
    """Solve part 1"""
    points = data[0]

    for instruction in data[1]:
        points = fold_paper(points, instruction)
        # for part 1, we only care about the first fold instruction
        break

    return len(points)

def part2(data):
    """Solve part 2"""
    points = data[0]

    for instruction in data[1]:
        points = fold_paper(points, instruction)

    print_points(points)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))