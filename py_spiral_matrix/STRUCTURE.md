# py_spiral_matrix — Structure ✅ (fait)

## 1. Entrée / Sortie
| | Type | Exemple |
|---|---|---|
| Entrée | `int n` | `3` |
| Sortie | `list[list[int]]` n×n | `[[1, 2, 3], [8, 9, 4], [7, 6, 5]]` |

## 2. Étapes (4 bornes qui se resserrent)
- [x] `n <= 0` : `[]`
- [x] Grille remplie de 0 : `[[0] * n for _ in range(n)]`
- [x] `val = 1`, bornes `nord = 0`, `sud = n - 1`, `ouest = 0`, `est = n - 1`
- [x] Tant que `val <= n * n` :
  - [x] ligne `nord`, de `ouest` à `est` (→), puis `nord += 1`
  - [x] colonne `est`, de `nord` à `sud` (↓), puis `est -= 1`
  - [x] ligne `sud`, de `est` à `ouest` (←), puis `sud -= 1`
  - [x] colonne `ouest`, de `sud` à `nord` (↑), puis `ouest += 1`
- [x] Renvoyer la grille

## 3. Outils Python
- `range(a, b + 1)` pour avancer, `range(a, b - 1, -1)` pour reculer
- `grille[ligne][colonne]`

## 4. Pièges
- `[[0] * n] * n` crée n fois LA MÊME ligne : utiliser la compréhension de liste
- Mettre à jour la borne APRÈS chaque côté, sinon les coins sont écrits deux fois
- Tester n pair (2, 4) et n impair (1, 3, 5)

## 5. Tests
| Entrée | Attendu |
|---|---|
| `1` | `[[1]]` |
| `2` | `[[1, 2], [4, 3]]` |
| `3` | `[[1, 2, 3], [8, 9, 4], [7, 6, 5]]` |
| `0` | `[]` |
