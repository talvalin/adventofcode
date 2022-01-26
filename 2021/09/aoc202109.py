# aoc202109.py

import pathlib
import sys

def create_heightmap(width, height):
    return [[0 for i in range(width)] for j in range(height)]

def parse(puzzle_input):
    """Parse input"""
    input = puzzle_input.split()
    grid = create_heightmap(len(input[0]), len(input))
    for i,y in enumerate(input):
        for j,x in enumerate(y):
            grid[i][j] = int(x)
    
    return grid

def get_low_points(grid):
    low_points = []
    low_point_flag = True
    height = len(grid)
    width = len(grid[0])

    # check surrounding points
    for i,y in enumerate(grid):
        for j,x in enumerate(y):
            # check left
            if j-1>=0 and grid[i][j] >= grid[i][j-1]:
                low_point_flag = False
            # check right
            if j+1<=width-1 and grid[i][j] >= grid[i][j+1]:
                low_point_flag = False
            # check up
            if i-1>=0 and grid[i][j] >= grid[i-1][j]:   
                low_point_flag = False
            # check down
            if i+1<=height-1 and grid[i][j] >= grid[i+1][j]:
                low_point_flag = False
        
            # if low, add coordinates to low_points
            if low_point_flag:
                low_points.append((i,j))

            low_point_flag = True
    return low_points

def mark_basin(binary_grid, grid, height, width, y, x):
    """Recursive function to mark points belonging to a specific basin"""
    # end condition
    # if the point is a 9 in the heightmap, we've hit the edge of the basin
    # if the point is a 1 in the binary map, then we've already marked this point
    if grid[y][x] == 9 or binary_grid[y][x] == 1:
        return

    # mark basin point
    binary_grid[y][x] = 1

    # check up
    if y>=1:
        mark_basin(binary_grid, grid, height, width, y-1, x)
    # check down
    if y+1<=height-1:
        mark_basin(binary_grid, grid, height, width, y+1, x)
    # check left
    if x>=1:
        mark_basin(binary_grid, grid, height, width, y, x-1)
    # check right
    if x+1<=width-1:
        mark_basin(binary_grid, grid, height, width, y, x+1)


def get_basin_sizes(low_points, grid):
    basins = []
    basin_sizes = []
    height = len(grid)
    width = len(grid[0])

    for point in low_points:
        # create new binary basin grid
        binary_grid = create_heightmap(width, height)

        # mark basin
        mark_basin(binary_grid, grid, height, width, point[0], point[1])
        basins.append(binary_grid)
    
    # need to sum total of each basin in the list
    for basin in basins:
        total = 0
        for i,y in enumerate(basin):
            for j,x in enumerate(y):
                total += basin[i][j]
        basin_sizes.append(total)

    return basin_sizes

def calculate_risk_levels(low_points, data):
    low_points_total = sum([data[point[0]][point[1]] for point in low_points])
    return low_points_total + len(low_points)

def part1(data):
    """Solve part 1"""
    low_points = get_low_points(data)
    return calculate_risk_levels(low_points, data)

def part2(data):
    """Solve part 2"""
    low_points = get_low_points(data)
    basin_sizes = get_basin_sizes(low_points, data)
    basin_sizes.sort()
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

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