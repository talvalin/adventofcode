import re
from collections import Counter

def test_password(password):
    password_string = str(password)
    for i in range(len(password_string)):
        if (i > 0 and password_string[i] < password_string[i-1]):
            return False

    for c in Counter(password_string).values():
        if c >= 2:
            return True  
    return False

def test_password_v2(password):
    password_string = str(password)
    for i in range(len(password_string)):
        if (i > 0 and password_string[i] < password_string[i-1]):
            return False
  
    for c in Counter(password_string).values():
        if c == 2:
            return True  
    return False

def find_valid_password_count():
    password_min = 172851
    password_max = 675869

    total_part1 = sum([1 for x in range(password_min, password_max) if test_password(x)])
    total_part2 = sum([1 for x in range(password_min, password_max) if test_password_v2(x)])

    print("Part 1 total: ", total_part1)
    print("Part 2 total: ", total_part2)

def main():
    find_valid_password_count()

if __name__ == "__main__":
    main()