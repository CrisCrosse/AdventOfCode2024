import sys


def main_part_1() -> int:
    with open("/Users/chris.rossell/projects/AdventOfCode2024/AdventOfCode2024/src/day_6/input.txt", "r") as f:
        grid = list(map(list, map(str.strip, f.readlines())))

    num_rows = len(grid)
    num_cols = len(grid[0])

    r, c = get_start(grid)
    dr, dc = -1, 0
    visited = set()

    while True:
        visited.add((r, c))
        if not (0 <= r + dr < num_rows and 0 <= c + dc < num_cols):
            break
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc

    print(f"Part 1: {len(visited)}")
    return len(visited)


def get_start(grid):
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == "^":
                return (r, c)





def check_for_loop(grid, start_r, start_c):
    num_rows = len(grid)
    num_cols = len(grid[0])

    r, c = start_r, start_c
    dr, dc = -1, 0
    visited = set()

    while True:
        if (r, c, dr, dc) in visited:
            return True
        visited.add((r, c, dr, dc))
        if not (0 <= r + dr < num_rows and 0 <= c + dc < num_cols):
            return False
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc
        else:
            r += dr
            c += dc

def main_part_2() -> int:
    with open("/Users/chris.rossell/projects/AdventOfCode2024/AdventOfCode2024/src/day_6/input.txt", "r") as f:
        grid = list(map(list, map(str.strip, f.readlines())))

    num_rows = len(grid)
    num_cols = len(grid[0])
    start_r, start_c = get_start(grid)
    part2 = 0
    for ro in range(num_rows):
        for co in range(num_cols):
            if grid[ro][co] != ".":
                continue
            grid[ro][co] = "#"
            if check_for_loop(grid, start_r, start_c):
                part2 += 1
            grid[ro][co] = "."

    print(f"Part 2: {part2}")
    return part2
