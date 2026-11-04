def _flow_island(matrix, x, y):
    """ convertis la terre(1) en eau(0)

    Args:
        matrix (_type_): tableau 2d (carte)
        pos (_type_): terre trouver(position)
        return 1 (l'ile)
    """

    if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])
       or matrix[x][y] != '1'):
        return
    matrix[x][y] = '0'
    _flow_island(matrix, x-1, y)
    _flow_island(matrix, x+1, y)
    _flow_island(matrix, x, y-1)
    _flow_island(matrix, x, y+1)


def island_matrix_counter(matrix: list[list[str]]) -> int:
    """retourne le nombre d'ile dans la matrix
    . 1 = terre
    . 0 = eau

    matrix: list[list[str]] : carte 2d

    retour: retourne le nombre d'ile"""

    count = 0
    if matrix == []:
        return count

    line = len(matrix)
    col = len(matrix[0])

    for x in range(line):
        for y in range(col):
            if matrix[x][y] == '1':
                count += 1
                _flow_island(matrix, x, y)
    return count


if __name__ == "__main__":
    print(
        island_matrix_counter(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "1", "0", "0"],
                ["1", "1", "1", "1", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
    )
