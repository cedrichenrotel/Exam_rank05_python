def prism_detector(grid: list[str], pattern: str):

    if grid == [] or pattern == "":
        return []

    directions = [
        (0, 1, "H"),     # droite
        (1, 0, "V"),     # bas
        (1, 1, "D"),     # bas-droite
        (-1, 1, "A"),    # haut-droite
        (0, -1, "HR"),   # gauche
        (-1, 0, "VR"),   # haut
        (-1, -1, "DR"),  # haut-gauche
        (1, -1, "AR"),   # bas-gauche
    ]
    lines = len(grid)
    cols = len(grid[0])
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
