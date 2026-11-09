def compress(s: str) -> str:

    rst: str = ""
    if s == "":
        return rst

    i = 0
    while i < len(s):
        count = 1
        j = i + 1
        while j < len(s) and s[i] == s[j]:
            count += 1
            j += 1
        rst += s[i]
        if count > 1:
            rst += str(count)
        i += count
    return rst


def count_nb(s: str) -> int:
    nb: str = ""
    for c in s:
        if c.isdigit():
            nb += c
        else:
            break
    return int(nb)


def decompress(s: str) -> str:
    rst: str = ""
    if s == "":
        return rst

    for i in range(len(s)):
        nb: int = 1
        if not s[i].isdigit():
            rst += s[i]
        elif not s[i - 1].isdigit():
            nb = count_nb(s[i:])
            rst += s[i - 1] * (nb - 1)
    return rst


if __name__ == "__main__":

    print(compress("aabcccccaaa"))
    print("a2bc5a3")
    print()
    print(decompress("a2bc5a3"))
    print("aabcccccaaa")
    print()
    print(compress(""))
    print("sortie: """)
    print(decompress("a12"))
    print("sortie: 'aaaaaaaaaaaa'")