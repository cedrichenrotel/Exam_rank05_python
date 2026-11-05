def _count_char(s: str, c: str) -> int:
    count: int = 0
    for i in range(len(s)):
        if s[i] != c:
            break
        count += 1
    return count


def compress(s: str) -> str:
    rst = ""
    if s == "":
        return rst
    i = 0
    while i < len(s):
        rst += s[i]
        step = _count_char(s[i:], s[i])
        if step > 1:
            rst += str(step)
        i += step
    return rst


def _conv_nb(i: str) -> int:
    nb = ""
    for n in i:
        if n.isdigit():
            nb += n
        else:
            break
    return int(nb)


def decompress(s: str) -> str:
    rst = ""
    if s == "":
        return rst

    for i in range(len(s)):
        nb = 0
        if s[i].isdigit():
            if not s[i-1].isdigit():
                nb = _conv_nb(s[i:])
                rst += rst[-1] * (nb - 1)
        else:
            rst += s[i]

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