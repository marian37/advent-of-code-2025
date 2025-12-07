def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def part1(input):
    splitted = 0
    beams = set()
    beams.add(input[0].index("S"))
    for line in input[1:]:
        new_beams = set()
        for beam in beams:
            if line[beam] == "^":
                splitted += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams
    return splitted


def part2(input):
    timelines = [1 if input[0][x] == "S" else 0 for x in range(len(input[0]))]
    for line in input[1:]:
        # print(line, timelines)
        new_timelines = timelines.copy()
        for i in range(len(line)):
            if line[i] == "^":
                new_timelines[i] = 0
            if i - 1 >= 0 and line[i - 1] == "^":
                new_timelines[i] += timelines[i - 1]
            if i + 1 < len(line) and line[i + 1] == "^":
                new_timelines[i] += timelines[i + 1]
        timelines = new_timelines
    return sum(timelines)


testInput = readInput("07_test.txt")
assert part1(testInput) == 21
assert part2(testInput) == 40

input = readInput("07.txt")
print(part1(input))
print(part2(input))
