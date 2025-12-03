def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    return lines


def part1(input):
    result = 0
    for line in input:
        a = int(line[0])
        b = int(line[1])
        for c in range(2, len(line)):
            d = int(line[c])
            if b > a:
                a = b
                b = d
            elif d > b:
                b = d
        result += 10 * a + b
    return result


def part2(input, first_part=False):
    result = 0
    for line in input:
        dp = [["0" for x in range(13)] for y in range(len(line))]
        for j in range(len(line)):
            dp[j][1] = max(dp[j - 1][1], line[j])
        for r in range(2, 13):
            dp[r - 1][r] = line[:r]
            for i in range(r, len(line)):
                dp[i][r] = max(dp[i - 1][r], dp[i - 1][r - 1] + line[i])
        result += (
            int(dp[len(line) - 1][2]) if first_part else int(dp[len(line) - 1][12])
        )
    return result


testInput = readInput("03_test.txt")
assert part1(testInput) == 357
assert part2(testInput, True) == 357
assert part2(testInput) == 3121910778619

input = readInput("03.txt")
print(part1(input))
print(part2(input, True))
print(part2(input))
