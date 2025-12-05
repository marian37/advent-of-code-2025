def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    reading_ranges = True
    ranges = []
    ids = []
    for line in lines:
        if line == "":
            reading_ranges = False
            continue
        if reading_ranges:
            f, t = line.split("-")
            ranges.append((int(f), int(t)))
        else:
            ids.append(int(line))
    return ranges, ids


def overlap(r, f, t):
    fr, ft = r
    return (f >= fr and f <= ft) or (t >= fr and t <= ft) or (f <= fr and t >= ft)


def merge(r, f, t):
    fr, ft = r
    return (min(f, fr), max(t, ft))


def part1(input):
    ranges, ids = input
    result = 0
    for id in ids:
        for f, t in ranges:
            if id >= f and id <= t:
                result += 1
                break
    return result


def part2(input):
    ranges, _ = input
    new_ranges = []
    for added_range in ranges:
        f, t = added_range
        i = 0
        while i < len(new_ranges):
            if overlap(new_ranges[i], f, t):
                r = new_ranges.pop(i)
                f, t = merge(r, f, t)
                i = 0
            else:
                i += 1
        new_ranges.append((f, t))
    result = 0
    for f, t in new_ranges:
        result += t - f + 1
    return result


testInput = readInput("05_test.txt")
assert part1(testInput) == 3
assert part2(testInput) == 14

input = readInput("05.txt")
print(part1(input))
print(part2(input))
