def load_input():
    input = []
    with open('../aoc_inputs/2019/day03_input.txt') as file: 
        for line in file.read().splitlines(): 
            l = line.split(',') 
            input.append(l)
    return input

def lay_pipe(pipe, path_element):
    direction = path_element[:1]
    distance = int(path_element[1:])

    last_position_x, last_position_y = pipe[-1]

    if direction == 'U':
        pipeline = [[last_position_x, last_position_y + i] for i in range(1, distance+1)]
        pipe += pipeline
    elif direction == 'D':
        pipeline = [[last_position_x, last_position_y - i] for i in range(1, distance+1)]
        pipe += pipeline
    elif direction == 'L':
        pipeline = [[last_position_x - i, last_position_y] for i in range(1, distance+1)]
        pipe += pipeline
    elif direction == 'R':
        pipeline = [[last_position_x + i, last_position_y] for i in range(1, distance+1)]
        pipe += pipeline
    return pipe

def find_intersect(pipe1, pipe2):
    return [list(x) for x in set(map(tuple, pipe1)).intersection(map(tuple, pipe2))]  

def find_minimum_intersection_distance(pipe1, pipe2, intersection_points):
    intersection_distances = []
    for point in intersection_points:
        # calculate Manhatten distance
        if point == [0,0]:
            continue
        intersection_distances.append((point, abs(point[0]) + abs(point[1])))

    intersection_distances.sort(key=lambda intersection_distance: intersection_distance[1])   
    return intersection_distances[0][1]

def find_minimum_intersection_time(pipe1, pipe2, intersection_points):
    intersection_times = []
    for point in intersection_points:
        # calculate combined steps to intersection
        if point == [0,0]:
            continue
        pipe1_steps = pipe1.index(point)
        pipe2_steps = pipe2.index(point)
        intersection_times.append((point, pipe1_steps + pipe2_steps))
    intersection_times.sort(key=lambda intersection_time: intersection_time[1])
    return intersection_times[0][1]

def main():
    pipe1 = [[0,0]]
    pipe2 = [[0,0]]
    
    path1, path2 = load_input() 
    
    for path in path1:
        pipe1 = lay_pipe(pipe1, path)

    for path in path2:
        pipe2 = lay_pipe(pipe2, path)

    intersection_points = find_intersect(pipe1, pipe2)
    print(find_minimum_intersection_distance(pipe1, pipe2, intersection_points))
    print(find_minimum_intersection_time(pipe1, pipe2,intersection_points))

if __name__ == "__main__":
    main()