import string

vowels = ['a', 'e', 'i', 'o', 'u']

def load_input():
    with open('./2015/inputs/day05_input.txt') as input:
        return [x.strip() for x in input.readlines()]

def nice_string(word):
    word = word.lower()
    bad_strings = ['ab', 'cd', 'pq', 'xy']
    if any(x in word for x in bad_strings):
        return False
    if sum([1 for letter in word if letter in vowels]) < 3:
        return False
    for x in range(len(word)-1):
        if word[x] == word[x+1]:
            return True

def nicer_string(word):
    word = word.lower()
    pair_repeat = False
    separated_repeated_letter = False
    # check for a repeated pair
    for x in range(len(word)-1):
         substring = word[x] + word[x+1]
         # can we find the substring at an index greater than x?
         if word.count(substring) >= 2:
            pair_repeat = True
    # check for repeated letter with a letter in between
    for x in range(len(word)-2):
        if word[x] == word[x+2]:
            separated_repeated_letter = True
    return pair_repeat and separated_repeated_letter
    

def part1(words):
    nice_words = sum(1 for word in words if nice_string(word) == True)
    print("Part 1 nice words: ", nice_words)

def part2(words):
    nice_words = sum(1 for word in words if nicer_string(word) == True)
    print("Part 2 nice words: ", nice_words)

def main():
    words = load_input()
    part1(words)
    part2(words)

if __name__ == "__main__":
    main()