# py_graph_cycle_detector — Structure ✅ (fait)

## 1. Entrée / Sortie
| | Type | Exemple |
|---|---|---|
| Entrée | `dict[int, list[int]]` : nœud → voisins (graphe orienté) | `{0: [1], 1: [2], 2: [0]}` |
| Sortie | `bool` | `True` s'il y a un cycle, `False` sinon ou si le graphe est vide |

## 2. Étapes (DFS avec 2 ensembles)
- [x] Graphe vide : `False`
- [x] `fil = set()` : nœuds sur le chemin EN COURS
- [x] `termine = set()` : nœuds déjà entièrement explorés (pas de cycle depuis eux)
- [x] Fonction récursive `_visited(n)` :
  - [x] ajouter `n` à `fil`
  - [x] pour chaque voisin (`graph.get(n, [])`) :
    - [x] si le voisin est dans `fil`, c'est un CYCLE : `True`
    - [x] s'il n'est pas dans `termine` et que `_visited(voisin)` renvoie True : `True`
  - [x] retirer `n` de `fil`, l'ajouter à `termine`, renvoyer `False`
- [x] Lancer `_visited` sur chaque nœud pas encore dans `termine`
- [x] Rien trouvé : `False`

## 3. Outils Python
- `set()`, `.add()`, `.remove()`, `in`
- Fonction imbriquée qui accède à `fil` / `termine` / `graph`
- `graph.get(n, [])` pour un voisin qui n'est pas une clé du dict

## 4. Pièges
- Un seul ensemble « visité » ne suffit pas : `{0: [1, 2], 1: [2], 2: []}` n'a PAS de cycle, mais 2 est atteint deux fois
- Boucle sur soi-même `{0: [0]}` : c'est un cycle
- Graphe non connexe : il faut partir de chaque nœud, pas seulement du premier

## 5. Tests
| Entrée | Attendu |
|---|---|
| `{0: [1], 1: [2], 2: [0]}` | True |
| `{0: [1], 1: [2], 2: []}` | False |
| `{}` | False |
| `{0: [1], 1: [2], 2: [1]}` | True |
| `{0: [1, 2], 1: [2], 2: []}` | False |
| `{0: [0]}` | True |
