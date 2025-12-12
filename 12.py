def readInput(fileName):
    file = open(fileName, "r")
    lines = file.read().splitlines()
    file.close()
    presents = []
    regions = []
    temp = []
    for line in lines:
        if line == "":
            presents.append(temp)
            temp = []
        else:
            colon_position = line.find(":")
            if colon_position == -1:
                temp.append(line)
            elif colon_position == len(line) - 1:
                continue
            else:
                wl, desc = line.split(":")
                width, length = wl.split("x")
                d = list(map(int, desc.strip().split()))
                regions.append((int(width), int(length), d))
    return presents, regions


def calculate_presents_area(presents):
    presents_area = []
    for present in presents:
        area = 0
        for line in present:
            for c in line:
                if c == "#":
                    area += 1
        presents_area.append(area)
    return presents_area


def part1(input):
    presents, regions = input
    presents_area = calculate_presents_area(presents)
    result = 0
    for region in regions:
        width, length, desc = region
        area = width * length
        p_area = sum([presents_area[i] * desc[i] for i in range(len(desc))])
        if area > p_area:
            result += 1
    return result


input = readInput("12.txt")
print(part1(input))
