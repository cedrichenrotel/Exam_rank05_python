def generate_spiral(n: int) -> list[list[int]]:
    grille = [[0] * n for _ in range(n)]
    val: int = 1
    total_case = n * n
    nord: int = 0
    est: int = n - 1
    sud: int = n - 1
    ouest: int = 0

    if n <= 0:
        return []

    while val <= total_case:
        # nord
        for col in range(ouest, est + 1):
            grille[nord][col] = val
            val += 1
        nord += 1
        # est
        for lig in range(nord, sud + 1):
            grille[lig][est] = val
            val += 1
        est -= 1
        # sud
        for col in range(est, ouest - 1, -1):
            grille[sud][col] = val
            val += 1
        sud -= 1
        # ouest
        for lig in range(sud, nord - 1, -1):
            grille[lig][ouest] = val
            val += 1
        ouest += 1

    return grille


def main():
    print("spiral")
    print(generate_spiral(3))


if __name__ == "__main__":
    main()
