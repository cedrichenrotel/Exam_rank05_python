def _verif(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    count: int = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count == 1


def word_ladder(start: str, end: str, sentence: list[str]) -> int:
    if end not in sentence:
        return 0
    level: list[str] = [start]
    visited: set[str] = {start}
    count: int = 1

    while level:
        if end in level:
            return count
        level_next: list[str] = []
        for word in level:
            for w in sentence:
                if w not in visited and _verif(word, w):
                    visited.add(w)
                    level_next.append(w)
        level = level_next
        count += 1
    return 0


if __name__ == "__main__":
    print(
        word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        )
    print("5")
    print()
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
    print("0")
