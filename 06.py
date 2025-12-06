def readInput(fileName):
    file = open(fileName, "r")
    raw_lines = file.read().splitlines()
    file.close()
    lines = []
    for raw_line in raw_lines[:-1]:
        lines.append([int(x) for x in raw_line.split()])
    lines.append(raw_lines[-1].split())
    return lines, raw_lines


def part1(input):
    result = 0
    for c in range(len(input[0])):
        multiply = input[-1][c] == "*"
        temp = 1 if multiply else 0
        for r in range(len(input) - 1):
            if multiply:
                temp *= input[r][c]
            else:
                temp += input[r][c]
        result += temp
    return result


def part2(input):
    result = 0
    numbers = []
    for c in range(len(input[0]) - 1, -1, -1):
        number = ""
        for r in range(len(input) - 1):
            if input[r][c] != " ":
                number += input[r][c]
        if number == "":
            continue
        numbers.append(int(number))
        if input[-1][c] == "*":
            temp = 1
            for n in numbers:
                temp *= n
            result += temp
            numbers.clear()
        elif input[-1][c] == "+":
            result += sum(numbers)
            numbers.clear()
    return result


testInputPart1, testInputPart2 = readInput("06_test.txt")
assert part1(testInputPart1) == 4277556
assert part2(testInputPart2) == 3263827

inputPart1, inputPart2 = readInput("06.txt")
print(part1(inputPart1))
print(part2(inputPart2))
