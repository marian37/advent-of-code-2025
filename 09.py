from collections import deque


def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    tiles = []
    for line in lines:
        x, y = line.split(",")
        tiles.append((int(x), int(y)))
    return tiles


def floodfill(tiles, seed):
    seed_x, seed_y = seed
    queue = deque()
    queue.append((seed_x, seed_y))
    while queue:
        x, y = queue.popleft()
        if tiles[y][x] != " ":
            continue
        else:
            tiles[y][x] = "#"
        if x > 0:
            queue.append((x - 1, y))
        if x < len(tiles[0]) - 1:
            queue.append((x + 1, y))
        if y > 0:
            queue.append((x, y - 1))
        if y < len(tiles) - 1:
            queue.append((x, y + 1))


def check_rectangle(tiles, x1, y1, x2, y2):
    mnx = min(x1, x2)
    mxx = max(x1, x2)
    mny = min(y1, y2)
    mxy = max(y1, y2)
    for x in range(mnx, mxx + 1):
        for y in range(mny, mxy + 1):
            if tiles[y][x] == " ":
                return False
    return True


def part1(input):
    result = 0
    for i in range(len(input)):
        xi, yi = input[i]
        for j in range(i + 1, len(input)):
            xj, yj = input[j]
            result = max(result, abs(xi - xj + 1) * abs(yi - yj + 1))
    return result


def part2(input, seed):
    cols = set()
    for x, _ in input:
        cols.add(x)
    cols = sorted(list(cols))

    rows = set()
    for _, y in input:
        rows.add(y)
    rows = sorted(list(rows))

    tiles = [[" " for _ in range(len(cols))] for _ in range(len(rows))]

    for i in range(len(input)):
        xj, yj = input[i - 1]
        xj = cols.index(xj)
        yj = rows.index(yj)
        xi, yi = input[i]
        xi = cols.index(xi)
        yi = rows.index(yi)
        tiles[yj][xj] = "X"
        tiles[yi][xi] = "X"
        if yj == yi:
            for x in range(min(xj, xi) + 1, max(xj, xi)):
                tiles[yj][x] = "o"
        else:
            for y in range(min(yj, yi) + 1, max(yj, yi)):
                tiles[y][xj] = "o"

    floodfill(tiles, seed)

    max_rectangle = 0
    for i in range(len(input)):
        xi, yi = input[i]
        for j in range(i + 1, len(input)):
            xj, yj = input[j]
            rectangle_size = (abs(xi - xj) + 1) * (abs(yi - yj) + 1)
            if rectangle_size <= max_rectangle:
                continue
            if check_rectangle(
                tiles, cols.index(xi), rows.index(yi), cols.index(xj), rows.index(yj)
            ):
                # print(xi, yi, xj, yj, rectangle_size)
                max_rectangle = rectangle_size

    # print(cols)
    # print(rows)
    # for line in input:
    #     print(line)
    # for row in tiles:
    #     print("".join(row))
    return max_rectangle


testInput = readInput("09_test.txt")
assert part1(testInput) == 50
assert part2(testInput, (2, 1)) == 24

input = readInput("09.txt")
print(part1(input))
print(part2(input, (100, 50)))
