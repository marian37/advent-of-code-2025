def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def part1(input):
    last_position = 50
    positions = []
    positions.append(last_position)
    for line in input:
        dir = -1 if line[0] == "L" else 1
        length = int(line[1:])
        new_position = (last_position + dir * length) % 100
        positions.append(new_position)
        last_position = new_position
    return positions.count(0)


def part2(input):
    last_position = 50
    count = 0
    for line in input:
        dir = -1 if line[0] == "L" else 1
        length = int(line[1:])
        count += length // 100
        new_position = (last_position + dir * length) % 100
        if new_position == 0:
            count += 1
        elif last_position != 0:
            if dir == -1:
                if new_position > last_position:
                    count += 1
            else:
                if new_position < last_position:
                    count += 1
        # print(last_position, new_position, count)
        last_position = new_position
    return count


testInput = readInput("01_test.txt")
assert part1(testInput) == 3
assert part2(testInput) == 6
assert part2(["R1000"]) == 10

input = readInput("01.txt")
print(part1(input))
print(part2(input))
