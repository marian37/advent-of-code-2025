import re
import heapq
from z3 import Optimize, Int


def readInput(fileName):
    file = open(fileName, "r")
    raw_lines = file.read().splitlines()
    file.close()
    lines = []
    regex = r"\[(?P<lights>[^]]+)\]\s*(?P<wirings>[^]]+)\{(?P<joltage>[^]]+)\}"
    for raw_line in raw_lines:
        lights, wirings, joltage = re.match(regex, raw_line).groupdict().values()
        lines.append(
            (
                lights,
                [
                    list(map(int, nums.split(",")))
                    for nums in re.findall(r"\((\s*\d+(?:\s*,\s*\d+)*\s*)\)", wirings)
                ],
                [int(j) for j in joltage.split(",")],
            )
        )
    return lines


def get_num(lights):
    lights_num = 0
    for i, c in enumerate(lights):
        if c == "#":
            lights_num += 1 << i
    return lights_num


def dijkstra(target, size, wirings):
    MAX_VALUE = 1 << 31
    dist = [MAX_VALUE for _ in range(size)]
    dist[0] = 0
    queue = []
    heapq.heappush(queue, 0)
    while queue:
        u = heapq.heappop(queue)
        for wiring in wirings:
            v = u
            for k in wiring:
                v ^= 1 << k
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(queue, v)
    return dist[target]


def ilp(wirings, joltage):
    optimize = Optimize()
    vector = []
    for i in range(len(wirings)):
        vector.append(Int("w" + str(i)))
        optimize.add(vector[i] >= 0)
    for i, j in enumerate(joltage):
        v = []
        for k, wiring in enumerate(wirings):
            if i in wiring:
                v.append(vector[k])
        optimize.add(sum(v) == j)
    optimize.minimize(sum(vector))
    optimize.check()
    result = optimize.model()
    return sum(result[v].as_long() for v in vector)


def part1(input):
    result = 0
    for line in input:
        lights, wirings, _ = line
        lights_num = get_num(lights)
        size = 1 << len(lights)
        result += dijkstra(lights_num, size, wirings)
    return result


def part2(input):
    result = 0
    for line in input:
        _, wirings, joltage = line
        temp = ilp(wirings, joltage)
        result += temp
    return result


testInput = readInput("10_test.txt")
assert part1(testInput) == 7
assert part2(testInput) == 33

input = readInput("10.txt")
print(part1(input))
print(part2(input))
