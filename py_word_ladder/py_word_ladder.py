def _on_diff(a: str, b: str) -> bool:
    """verifie si les mots ont bien la meme longueur
    et qu'il y a un carctere different

    a: mot1
    b: mot2
    return: renvois true les conditions sont bien respecter sinon false"""

    if len(a) != len(b):
        return False
    count = sum(1 for i in range(len(a)) if a[i] != b[i])

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

        next_level = []
        for word in level:
            for w in sentence:
                if w not in visited and _on_diff(word, w):
                    visited.add(w)
                    next_level.append(w)
        level = next_level
        count += 1
    return 0


if __name__ == "__main__":
    print(word_ladder(
        "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
        ))
    print()
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
