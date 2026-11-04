# py_room_scheduler — Structure

## 1. Entrée / Sortie
| | Type | Exemple |
|---|---|---|
| Entrée | `list[list[int]]` : liste de `[début, fin]` | `[[0, 30], [5, 10], [15, 20]]` |
| Sortie | `dict` avec `"total_rooms"` et `"schedule"` | `{"total_rooms": 2, "schedule": [[[0, 30]], [[5, 10], [15, 20]]]}` |

```
schedule = [ salle1, salle2, ... ]
salle    = [ réunion, réunion, ... ]
réunion  = [début, fin]
```

## 2. Étapes
- [ ] Cas vide : renvoyer `{"total_rooms": 0, "schedule": []}`
- [ ] Trier les réunions par début : `meetings = sorted(meetings)`
- [ ] Créer `schedule = []`
- [ ] Pour chaque réunion :
  - [ ] parcourir les salles
  - [ ] fin de la dernière réunion de la salle : `salle[-1][1]`
  - [ ] si `salle[-1][1] <= début`, ajouter dans cette salle puis `break`
  - [ ] si aucune salle ne convient, `schedule.append([reunion])`
- [ ] Renvoyer `{"total_rooms": len(schedule), "schedule": schedule}`

## 3. Outils Python
- `sorted(liste)` renvoie une NOUVELLE liste triée (il faut récupérer le résultat)
- `for ... else` : le `else` s'exécute seulement si on n'a pas fait de `break`
- `from typing import Any`

## 4. Pièges
- `<=` et pas `<` : `[0, 10]` et `[10, 20]` peuvent partager une salle
- La clé s'appelle `"total_rooms"`, pas `"total"`
- Prendre la PREMIÈRE salle libre pour obtenir l'ordre attendu

## 5. Tests
| Entrée | Salles attendues |
|---|---|
| `[[0, 30], [5, 10], [15, 20]]` | 2 |
| `[[0, 10], [10, 20]]` | 1 |
| `[[15, 20], [0, 30], [5, 10]]` | 2 (vérifie le tri) |
| `[[1, 5], [2, 6], [3, 7]]` | 3 |
| `[]` | 0 |
