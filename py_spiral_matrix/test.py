def generate_spiral(n: int) -> list[list[int]]:

    grille: list[list[int]] = [[0] * n for _ in range(n)]
    nord: int = 0
    est: int = n - 1
    sud: int = n - 1
    ouest: int = 0
    total: int = n * n
    val: int = 1

    if n <= 0:
        return []
    while val <= total:
        for col in range(ouest, est + 1):
            grille[nord][col] = val
            val += 1
        nord += 1
        for lig in range(nord, sud + 1):
            grille[lig][est] = val
            val += 1
        est -= 1
        for col in range(est, ouest - 1, - 1):
            grille[sud][col] = val
            val += 1
        sud -= 1
        for lig in range(sud, nord - 1, - 1):
            grille[lig][ouest] = val
            val += 1
        ouest += 1

    return grille


if __name__ == "__main__":
    print(generate_spiral(3))
