def load_input():
    with open('../aoc_inputs/2021/day04_input.txt') as input:
        return input.read().splitlines()

def update_board(board, draw):
    for x, line in enumerate(board):
        for y, num in enumerate(line):
            if num[0] == draw:
                board[x][y] = (num[0], 1)

def has_bingo(board):
    # check rows
    for idx, row in enumerate(board):
        total = sum(1 for n in row if n[1] == 1)
        if total == 5:
            return True

    # check columns
    columns = [[y[x] for y in board] for x in range(len(board[0]))]
    for idx, column in enumerate(columns):
        total = sum(1 for n in column if n[1] == 1)
        if total == 5:
            return True

    # check top-left to bottom-right diagonal
    diagonal_tl_br = [[y for y in board[x][x]] for x in range(len(board[0]))]
    total = sum(1 for n in diagonal_tl_br if n[1] == 1)
    if total == 5:
        return True
    
    # check bottom-left to top-right diagonal
    diagonal_bl_tr = [[y for y in board[x][4-x]] for x in range(len(board[0]))]
    total = sum(1 for n in diagonal_bl_tr if n[1] == 1)
    if total == 5:
        return True

    return False

def calculate_score(board, draw):
    score = 0
    for x, line in enumerate(board):
        for y, num in enumerate(line):
            if num[1] == 0:
                score += num[0]
    return score * draw

def part1(boards, draws):
   for d in draws:
        for board in boards:
            update_board(board, d)
            if has_bingo(board):
                return calculate_score(board, d)

def part2(boards, draws):
    winning_boards = set()
    for d in draws:
        for idx, board in enumerate(boards):
            update_board(board, d)
            if has_bingo(board):
                winning_boards.add(idx)
                if len(winning_boards) == len(boards):
                    return calculate_score(board, d)

def main():
    input = load_input()
    numbers = [int(s) for s in input[0].split(',')]

    # strip white space from remaining input
    clean_input = [line for line in input[1:] if line.strip()]

    # load bingo boards and initialise
    boards = []
    for x in range(0, len(clean_input), 5):
        board = []
        for line in clean_input[x:x+5]:
            board.append([(int(y), 0) for y in line.split()])
        boards.append(board)

    # play bingo
    print(part1(boards, numbers))
    print(part2(boards, numbers))

if __name__ == "__main__":
    main()