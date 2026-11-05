def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:

    if graph == []:
        return False
    fil: set[int] = set()
    termine: set[int] = set()

    def _verif(n: int) -> bool:
        fil.add(n)
        for connect in graph.get(n, []):
            if connect in fil:
                return True
            if connect not in termine and _verif(connect):
                return True
        fil.remove(n)
        termine.add(n)
        return False

    for noeud in graph:
        if noeud not in termine and _verif(noeud):
            return True
    return False


if __name__ == "__main__":

    print(py_graph_cycle_detector({0: [1], 1: [2], 2: [0]}))
    print("True")
    print()
    print(py_graph_cycle_detector({0: [1], 1: [2], 2: []}))
    print("False")
    print()
    print(py_graph_cycle_detector({}))
    print("False")
