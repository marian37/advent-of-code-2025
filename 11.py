def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    graph = {}
    for line in lines:
        v, raw_edges = line.split(":")
        edges = raw_edges.strip().split()
        graph[v] = edges
    return graph


def dfs(input, source, target):
    result = 0
    stack = []
    stack.append(source)
    while stack:
        v = stack.pop()
        if v == target:
            result += 1
            continue
        if v in input:
            for edge in input[v]:
                stack.append((edge))
    return result


def find_next(input, remaining_vertices):
    for v in remaining_vertices:
        found = False
        for u in input:
            if u == v:
                continue
            if v in input[u]:
                found = True
                break
        if not found:
            return v
    return None


def top_sort(input):
    sorted_vertices = []
    remaining_vertices = set(input.keys())
    remaining_vertices.add("out")
    while remaining_vertices:
        curr = find_next(input, remaining_vertices)
        sorted_vertices.append(curr)
        remaining_vertices.remove(curr)
        if curr in input:
            input.pop(curr)
    return sorted_vertices


def reverse(input):
    reversed_graph = {}
    for u in input:
        for v in input[u]:
            if v not in reversed_graph:
                reversed_graph[v] = []
            reversed_graph[v].append(u)
    return reversed_graph


def part1(input):
    return dfs(input, "you", "out")


def part2(input):
    sorted_graph = top_sort(input.copy())
    reversed_graph = reverse(input)
    dp = [0 for _ in range(len(sorted_graph))]
    fft_index = sorted_graph.index("fft")
    dac_index = sorted_graph.index("dac")
    for i, v in enumerate(sorted_graph):
        if v == "svr":
            dp[i] = 1
        else:
            rev = reversed_graph[v]
            if "fft" in rev:
                dp[i] = dp[sorted_graph.index("fft")]
            elif "dac" in rev:
                dp[i] = dp[sorted_graph.index("dac")]
            else:
                if i <= fft_index:
                    dp[i] = sum([dp[sorted_graph.index(u)] for u in rev])
                elif i <= dac_index:
                    dp[i] = sum(
                        [
                            (
                                dp[sorted_graph.index(u)]
                                if sorted_graph.index(u) >= fft_index
                                else 0
                            )
                            for u in rev
                        ]
                    )
                else:
                    dp[i] = sum(
                        [
                            (
                                dp[sorted_graph.index(u)]
                                if sorted_graph.index(u) >= dac_index
                                else 0
                            )
                            for u in rev
                        ]
                    )
    return dp[sorted_graph.index("out")]


testInput = readInput("11_test.txt")
assert part1(testInput) == 5
testInput2 = readInput("11_test2.txt")
assert part2(testInput2) == 2

input = readInput("11.txt")
print(part1(input))
print(part2(input))
