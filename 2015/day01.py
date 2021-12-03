from collections import Counter

def load_input():
    with open('./2015/inputs/day01_input.txt') as input:
        return input.readline()

def part1(directions):
    c = Counter(directions)
    print("Floor:", c['('] - c[')'])

def part2(directions):
    count = 0
    for index, element in enumerate(directions):
        if count == -1:
            print("Character:", index)
            break
        if element == '(':
            count += 1
        elif element == ')':
            count -= 1

def main():
    directions = load_input()
    part1(directions)
    part2(directions)

if __name__ == "__main__":
    main()