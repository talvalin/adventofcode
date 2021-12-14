import itertools

def load_input():
    with open('../aoc_inputs/2021/day05_input.txt') as input:
        return input.read().splitlines()

def update_grid(grid, line_segment, diagonals):
    x1,y1,x2,y2 = line_segment
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    if x1==x2:
        # horizontals
        for i in range(min_y, max_y+1):
            grid[x1][i] += 1
    elif y1==y2:
        # verticals
        for i in range(min_x, max_x+1):
            grid[i][y1] += 1
    else:
        if diagonals:
            # diagonals
            x_step = 1 if x1 < x2 else -1
            y_step = 1 if y1 < y2 else -1
            for i,j in zip(range(x1, x2+x_step, x_step), range(y1, y2+y_step, y_step)):
                grid[i][j] +=1

def calculate_overlaps(grid, grid_size):
    # do calculation
    total = 0
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x][y] >= 2:
                total += 1
    return total

def print_grid(grid, grid_size):
    for y in range(grid_size):
        output_line = ''
        for x in range(grid_size):
            if grid[x][y]:
                output_line += str(grid[x][y])
            else:
                output_line += '.'
    print(output_line)

def part1(grid, line_segments, grid_size):
    for seg in line_segments:
        update_grid(grid, seg, False)
    print(calculate_overlaps(grid, grid_size))

def part2(grid, line_segments, grid_size):
    for seg in line_segments:
        update_grid(grid, seg, True)
    print(calculate_overlaps(grid, grid_size))

def main():
    input = load_input()
    line_segments = []
    for line in input:
        line = line.replace(' -> ', ',')
        item = [int(x) for x in line.split(',')]
        line_segments.append(item)
        
    # get largest number to set grid size
    flattened = set(itertools.chain.from_iterable(line_segments))
    grid_size = sorted(flattened)[-1] + 1
    grid = [[0 for i in range(grid_size)] for j in range(grid_size)]
    part1(grid, line_segments, grid_size)
    part2(grid, line_segments, grid_size)

if __name__ == "__main__":
    main()