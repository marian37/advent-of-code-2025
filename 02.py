def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines[0]


def part1(input):
    result = 0
    ranges = input.split(",")
    for rn in ranges:
        f, t = rn.split("-")
        s = f[: len(f) // 2 if len(f) > 1 else 1]
        ss = s + s
        while (iss := int(ss)) <= int(t):
            if iss >= int(f):
                result += iss
            s = str(int(s) + 1)
            ss = s + s
    return result


def part2(input):
    result = 0
    ranges = input.split(",")
    for rn in ranges:
        f, t = rn.split("-")
        invalid = set()
        for length in range(1, len(t) // 2 + 1):
            rest = len(f) - length
            if length == 1 and len(t) > len(f):
                for rep in range(1, int(t[:length]) + 1):
                    s = str(rep) + str(rep)
                    si = int(s)
                    while si <= int(t):
                        if si >= int(f) and len(s) > 1:
                            invalid.add(si)
                        s = s + str(rep)
                        si = int(s)
            for rep in range(int(f[:length]), int(t[: len(t) - rest]) + 1):
                s = str(rep) + str(rep)
                si = int(s)
                while si <= int(t):
                    if si >= int(f) and len(s) > 1:
                        invalid.add(si)
                    s = s + str(rep)
                    si = int(s)
        result += sum(invalid)
    return result


testInput = readInput("02_test.txt")
assert part1(testInput) == 1227775554
assert part2(testInput) == 4174379265

input = readInput("02.txt")
print(part1(input))
print(part2(input))
