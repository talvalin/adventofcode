# aoc202111.py

import pathlib
import sys

def create_matrix(height, width):
    return [[0 for i in range(width)] for j in range(height)]

def parse(puzzle_input):
    """Parse input"""
    input = puzzle_input.split()
    grid = create_matrix(len(input), len(input[0]))
    for j,y in enumerate(input):
        for i,x in enumerate(y):
            grid[j][i] = int(x)

    return grid

def increment_energy_level(grid, height, width):
    for j in range(height):
        for i in range(width):
            grid[j][i] +=1

def mark_flashes(grid, flash_grid, height, width):
    pass

def count_flashes(grid):
    height = len(grid)
    width = len(grid[0])

    # increment energy levels of all octopuses
    increment_energy_level(grid, height, width)
    
    # initialize a binary flash map
    binary_flash_map = create_matrix(height, width)

    # recursively mark flashes and update matrix
    for j,y in enumerate(grid):
        for i,_ in enumerate(y):
            if grid[j][i] > 9:
                mark_flashes(binary_flash_map, grid, height, width, j, i)

    # sum elements of the binary flash map
    flash_total = sum(map(sum, binary_flash_map))

    # reset energy levels for flashing octopuses
    for j in range(height):
        for i in range(width):
            if grid[j][i] > 9:
                grid[j][i] = 0
    
    return flash_total

def get_neighbours(height, width, y, x):
    neighbours = []
    for j in range(max(0,y-1), min(height, y+2)):
        for i in range(max(0,x-1), min(width, x+2)):
            if j==y and i==x:
                continue
            else:
                neighbours.append((j,i))

    return neighbours

def mark_flashes(binary_grid, grid, height, width, y, x):
    """Recursive function to mark points belonging to a specific basin"""
    if binary_grid[y][x] == 1:
        return

    # mark flash
    binary_grid[y][x] = 1

    # get a list of neighbours
    neighbours = get_neighbours(height, width, y, x)
    for neighbour in neighbours:
        nj, ni = neighbour
        grid[nj][ni] += 1
        if grid[nj][ni] > 9:
            mark_flashes(binary_grid, grid, height, width, nj, ni)

def part1(data, steps):
    """Solve part 1"""
    flashes = 0
    for _ in range(0, steps):
        flashes += count_flashes(data)
    return flashes

def part2(data):
    """Solve part 2"""
    step_count = 1
    while count_flashes(data) != 100:
        step_count += 1
    
    return step_count

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    data2 = parse(puzzle_input)
    solution1 = part1(data, 100)
    solution2 = part2(data2)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))