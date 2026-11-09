def generate_spiral(n: int) -> list[list[int]]:

    grille: list[list[int]] = [[0] * n for _ in range(n)]
    total: int = n * n
    val: int = 1
    nord: int = 0
    est: int = n - 1
    sud: int = n - 1
    ouest: int = 0

    while val < total:
        # nord
        for col in range(ouest, est + 1):
            grille[nord][col] = val
            val += 1
        nord += 1
        # est
        for line in range(nord, sud + 1):
            grille[line][est] = val
            val += 1
        est -= 1
        # sud
        for col in range(est, ouest - 1, -1):
            grille[sud][col] = val
            val += 1
        sud -= 1
        # ouest
        for line in range(sud, nord - 1, - 1):
            grille[line][ouest] = val
            val += 1
        ouest += 1

    for ligne in grille:
        print(ligne)

    return grille


if __name__ == "__main__":
    # print(generate_spiral(3))
    # print("[[1, 2, 3], [8, 9, 4], [7, 6, 5]]")
    # print()
    # print(generate_spiral(1))
    # print("[[1]]")
    # print()
    print(generate_spiral(3))
    print("[[]]")
