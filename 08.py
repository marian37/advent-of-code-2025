def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    boxes = []
    for line in lines:
        x, y, z = line.split(",")
        boxes.append((int(x), int(y), int(z)))
    return boxes


def get_box_dist(box1, box2):
    return (
        (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2
    )


def get_dist(input):
    dist = []
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            dist.append((get_box_dist(input[i], input[j]), i, j))
    dist.sort(key=lambda triple: triple[0])
    return dist


def part1(input, pairs):
    dist = get_dist(input)
    circuits = [i for i in range(len(input))]
    for _, i, j in dist[:pairs]:
        ci = circuits[i]
        cj = circuits[j]
        mx = max(ci, cj)
        mn = min(ci, cj)
        for k in range(len(circuits)):
            if circuits[k] == mx:
                circuits[k] = mn
    circuit_stat = []
    for i in range(len(circuits)):
        circuit_stat.append((circuits.count(i), i))
    circuit_stat.sort(key=lambda pair: pair[0], reverse=True)
    result = 1
    for i in range(3):
        result *= circuit_stat[i][0]
    return result


def part2(input):
    dist = get_dist(input)
    circuits = [i for i in range(len(input))]
    for _, i, j in dist:
        ci = circuits[i]
        cj = circuits[j]
        mx = max(ci, cj)
        mn = min(ci, cj)
        if mx != mn:
            for k in range(len(circuits)):
                if circuits[k] == mx:
                    circuits[k] = mn
        if max(circuits) == 0:
            return input[i][0] * input[j][0]
    return None


testInput = readInput("08_test.txt")
assert part1(testInput, 10) == 40
assert part2(testInput) == 25272

input = readInput("08.txt")
print(part1(input, 1000))
print(part2(input))
