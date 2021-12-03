def load_input():
    with open('./inputs/day01_input.txt') as input:
        return [int(line) for line in input.readlines()]

def part1(depths):
    count = sum([a < b for a, b in zip(depths, depths[1:])])
    print(count)

# since our sliding window check is (a + b + c) < (b + c + d), we can simplify this to a < d
def part2(depths):
    count = sum(a < b for a, b in zip(depths, depths[3:]))
    print(count)

def main():
    depths = load_input()
    part1(depths)
    part2(depths)

if __name__ == "__main__":
    main()