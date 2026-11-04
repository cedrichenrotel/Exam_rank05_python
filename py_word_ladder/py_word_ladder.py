def _on_diff(a: str, b: str) -> bool:
    """verif si les ont bien la meme longueur
    et qu'il y a un carctere different

    a: mot1
    b: mot2
    return: renvois true les conditions sont bien respecter sinon false"""

    if len(a) != len(b):
        return False
    count = sum(1 for i in range(len(a)) if a[i] != b[i])

    return count == 1


def word_ladder(start: str, end: str, sentence: list[str]) -> int:

    rst = 0
    if end not in sentence:
        return rst

    queue: list[tuple[str, int]] = [(start, 1)]
    visited: dict[str, int] = {start}

    while len(queue) > 0:
        word = queue.pop(0)
        if word[0] == end:
            return word[1]
        else:
            if _on_diff(start, word[0]) and word[0] not in visited:
                visited.add(word[0])
                queue.append((w, word[1] + 1))
    return rst


if __name__ == "__main__":
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    print()
    print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
