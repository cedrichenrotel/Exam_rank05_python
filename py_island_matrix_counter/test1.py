def _submerge_island(matrix: list[list[str]], line: int, col: int) -> None:

    if (
        line < 0 or line >= len(matrix) or
        col < 0 or col >= len(matrix[0]) or
        matrix[line][col] != "1"
    ):
        return
    matrix[line][col] = "0"
    _submerge_island(matrix, line+1, col)
    _submerge_island(matrix, line-1, col)
    _submerge_island(matrix, line, col+1)
    _submerge_island(matrix, line, col-1)


def island_matrix_counter(matrix: list[list[str]]) -> int:
    rst: int = 0
    if matrix == []:
        return rst

    lines: int = len(matrix)
    cols: int = len(matrix[0])

    for line in range(lines):
        for col in range(cols):
            if matrix[line][col] == "1":
                rst += 1
                _submerge_island(matrix, line, col)
    return rst


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
    print("1")
    print()
    print(
        island_matrix_counter(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
    )
    print("3")
    print()
    print(island_matrix_counter([]))
    print("0")
