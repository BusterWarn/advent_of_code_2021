import re

class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
    
    def __str__(self):
        return "[%d, %d]" %(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

def main():
    lines = []
    with open("input.txt") as fp:
        line = fp.readline()
        while line:
            line = re.sub("\n", "", line)
            if len(line) == 0:
                break
            lines.append([int(s) for s in line])
            line = fp.readline()

    problem_1(lines)
    problem_2(lines)

def problem_1(lines):
    
    risks = []
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if is_lowpoint(lines, x, y):
                risks.append(lines[x][y] + 1)
    print("Problem 1: %d" %(sum(risks)))

def problem_2(lines):

    basin_lowpoints = []
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if is_lowpoint(lines, x, y):
                basin_lowpoints.append(coordinate(x, y))
    
    sizes = [0, 0, 0]
    for lowpoints in basin_lowpoints:
        sizes.append(len(explore_basin(lines, lowpoints)))
        sizes.sort()
        del sizes[0]
    
    print("Problem 2: %d" %(sizes[0] * sizes[1] * sizes[2]))

def is_lowpoint(lines, x, y):
    if x > 0:
        if lines[x - 1][y] <= lines[x][y]:
            return False
    if x < len(lines) - 1:
        if lines[x + 1][y] <= lines[x][y]:
            return False
    if y > 0:
        if lines[x][y - 1] <= lines[x][y]:
            return False
    if y < len(lines[x]) - 1:
        if lines[x][y + 1] <= lines[x][y]:
            return False
    return True

def explore_basin(lines, lowpoint):
    explore = {lowpoint}
    basin = set()

    while len(explore) > 0:
        coord = explore.pop()
        basin.add(coord)
        basin_height = lines[coord.x][coord.y]

        if coord.x > 0:
            height = lines[coord.x - 1][coord.y]
            if height > basin_height and height != 9:
                explore.add(coordinate(coord.x - 1, coord.y))

        if coord.x < len(lines) - 1:
            height = lines[coord.x + 1][coord.y]
            if height > basin_height and height != 9:
                explore.add(coordinate(coord.x + 1, coord.y))

        if coord.y > 0:
            height = lines[coord.x][coord.y - 1]
            if height > basin_height and height != 9:
                explore.add(coordinate(coord.x, coord.y - 1))

        if coord.y < len(lines[coord.x]) - 1:
            height = lines[coord.x][coord.y + 1]
            if height > basin_height and height != 9:
                explore.add(coordinate(coord.x, coord.y + 1))

    return basin




main()