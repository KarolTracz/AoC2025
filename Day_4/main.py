with open('input.txt') as f:
# with open('input_test.txt') as f:
    raw_input = [i.strip() for i in f.readlines()]


def main():
    result = 0

    old_puzzle = raw_input
    new_puzzle = old_puzzle.copy()
    removed = []

    for y, row in enumerate(old_puzzle):
        for x, char in enumerate(row):
            if char == '@':
                if check_neighbor(puzzle_input=raw_input, pos=(y, x)):
                    result += 1
                    removed.append((y, x,))
    print(result)
    for pos in removed:
        new_puzzle_copy = new_puzzle.copy()
        row = list(new_puzzle_copy[pos[0]])
        row[pos[1]] = '.'
        new_puzzle_copy[pos[0]] = ''.join(row)
        new_puzzle = new_puzzle_copy

    while True:
        if new_puzzle != old_puzzle:
            old_puzzle = new_puzzle

            for y, row in enumerate(old_puzzle):
                for x, char in enumerate(row):
                    if char == '@':
                        if check_neighbor(puzzle_input=old_puzzle, pos=(y, x)):
                            result += 1
                            removed.append((y, x,))
        else:
            break

        for pos in removed:
            new_puzzle_copy = new_puzzle.copy()
            row = list(new_puzzle_copy[pos[0]])
            row[pos[1]] = '.'
            new_puzzle_copy[pos[0]] = ''.join(row)
            new_puzzle = new_puzzle_copy
    print(result)


def get_puzzle_size(puzzle_input: list[str]) -> tuple[int, int]:
    return len(puzzle_input), len(puzzle_input[0])

size = get_puzzle_size(raw_input)

def check_neighbor(puzzle_input: list[str], pos: tuple[int, int]) -> bool:
    counter_rolls = 0

    neighbors = (
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1)
    )

    for neighbor in neighbors:
        new_pos = pos[0]-neighbor[0], pos[1]-neighbor[1]
        y, x = new_pos
        if y not in range(0, size[0]) or x not in range(0, size[1]):
            continue
        if puzzle_input[y][x] == '@':
            # print(f'for pos:{pos} neighbor {y}, {x}')
            counter_rolls += 1
        if counter_rolls > 3:
            return False

    return True


if __name__ == '__main__':
    main()
