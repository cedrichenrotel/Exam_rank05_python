def compress(s: str) -> str:

    rst: str = ""
    i = 0
    while i < len(s):
        j = i + 1
        count = 1
        while j < len(s) and s[j] == s[i]:
            count += 1
            j += 1
        rst += s[i]
        if count > 1:
            rst += str(count)
        i += count
    return rst


def decompress(s: str) -> str:

    rst = ""
    i = 0
    while i < len(s):
        c = s[i]
        i += 1
        nb = ""
        while i < len(s) and s[i].isdigit():
            nb += s[i]
            i += 1
        if nb == "":
            rst += c
        else:
            rst += c * int(nb)
    return rst


def main():
    print("compress")
    print(compress("aabcccccaaa"))
    print("\ndecompress")
    print(decompress("a2bc5a3"))


if __name__ == "__main__":
    main()
