def prism_detector(grid: list[str], pattern: str):

    rst: list[tuple[int, int, str]] = []
    if grid == [] or pattern == "":
        return rst

    direction: list[tuple[int, int, str]] = [
        (-1, 0, "N"),
        (-1, 1, "NE"),
        (0, 1, "E"),
        (1, 1, "SE"),
        (1, 0, "S"),
        (1, -1, "SO"),
        (0, -1, "O"),
        (-1, -1, "NO"),
    ]
    lines: int = len(grid)
    cols: int = len(grid[0])
    for line in range(lines):
        for col in range(cols):
            for dir in direction:
                for k in range(len(pattern)):
                    pos_kl: int = line + k * dir[0]
                    pos_kc: int = col + k * dir[1]
                    if (
                        pos_kl < 0
                        or pos_kl >= lines
                        or pos_kc < 0
                        or pos_kc >= cols
                        or grid[pos_kl][pos_kc] != pattern[k]
                    ):
                        break
                else:
                    rst.append((line, col, dir[2]))
    return rst


if __name__ == "__main__":
    print(prism_detector(["CAT", "A..", "T.."], "CAT"))
    print('[(0, 0, "H"), (0, 0, "V")]')
    print()
    print(prism_detector([], "CAT"))
    print("[]")
