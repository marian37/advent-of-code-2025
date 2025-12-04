def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


neighbours = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def can_be_removed(input, r, c):
    count = 0
    for nr, nc in neighbours:
        row = r + nr
        col = c + nc
        if row >= 0 and row < len(input) and col >= 0 and col < len(input[row]):
            if input[col][row] == "@":
                count += 1
    return count < 4


def remove(input, to_be_removed):
    new_input = []
    for row in range(len(input)):
        new_input.append(input[row])
    for c, r in to_be_removed:
        new_input[r] = new_input[r][:c] + "." + new_input[r][c + 1 :]
    return new_input


def part1(input):
    result = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[c][r] == ".":
                continue
            if can_be_removed(input, r, c):
                result += 1
    return result


def part2(input):
    to_be_removed = set()
    first = True
    result = 0
    while len(to_be_removed) or first:
        first = False
        to_be_removed.clear()
        for r in range(len(input)):
            for c in range(len(input[r])):
                if input[c][r] == ".":
                    continue
                if can_be_removed(input, r, c):
                    result += 1
                    to_be_removed.add((r, c))
        input = remove(input, to_be_removed)
    return result


testInput = readInput("04_test.txt")
assert part1(testInput) == 13
assert part2(testInput) == 43

input = readInput("04.txt")
print(part1(input))
print(part2(input))
