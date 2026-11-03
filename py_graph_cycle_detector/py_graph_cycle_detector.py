def py_graph_cycle_detector(graph: dict[int, list[int]]) -> bool:

    if graph == {}:
        return False

    fil = set()
    termine = set()

    def _visited(n: int) -> bool:
        """explore depuis le noeud(n) et cherche un cycle

        Args:
            n (int): noeud actuel

        Returns:
            bool: true si un cycle est atteignable
        """
        fil.add(n)

        for voisin in graph.get(n, []):
            if voisin in fil:
                return True
            if voisin not in termine and _visited(voisin):
                return True
        fil.remove(n)
        termine.add(n)
        return False
    for noeud in graph:
        if noeud not in termine and _visited(noeud):
            return True

    return False


if __name__ == "__main__":
    print(py_graph_cycle_detector({0: [1], 1: [2], 2: [0]}))   # True
    print(py_graph_cycle_detector({0: [1], 1: [2], 2: []}))    # False
    print(py_graph_cycle_detector({}))                          # False
    print(py_graph_cycle_detector({0: [1], 1: [2], 2: [1]}))   # True
    print(py_graph_cycle_detector({0: [1, 2], 1: [2], 2: []})) # False (2 chemins, pas de cycle)
    print(py_graph_cycle_detector({0: [0]}))                    # True (boucle sur soi-même)