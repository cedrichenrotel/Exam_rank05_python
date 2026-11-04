def prism_detector(grid: list[str], pattern: str):

    if grid == [] or pattern == "":
        return []

    directions = [
        (-1, 0, "N"),
        (-1, 1, "NE"),
        (0, 1, "E"),
        (1, 1, "SE"),
        (1, 0, "S"),
        (1, -1, "SO"),
        (0, -1, "O"),
        (-1, -1, "NO"),
    ]
    cols = len(grid)
    lines = len(grid[0])
    rst = []

    for line in range(lines):
        for col in range(cols):
            for dir in directions:
                for k in range(len(pattern)):
                    ld = line + k * dir[0]
                    lc = col + k * dir[1]
                    if (ld < 0 or ld >= len(grid)
                        or lc < 0 or lc >= len(grid[0])
                       or grid[ld][lc] != pattern[k]):
                        break
                else:
                    rst.append((col, line, dir[2]))
    return rst


if __name__ == "__main__":
    print(prism_detector(["CAT", "A..", "T.."], "CAT"))
