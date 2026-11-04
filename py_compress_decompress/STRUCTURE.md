# py_compress_decompress — Structure ✅ (fait)

## 1. Entrée / Sortie
| Fonction | Entrée | Sortie |
|---|---|---|
| `compress` | `"aabcccccaaa"` | `"a2bc5a3"` |
| `decompress` | `"a2bc5a3"` | `"aabcccccaaa"` |
| `compress` | `""` | `""` |

## 2. Étapes — compress
- [x] `rst = ""`, `i = 0`
- [x] Tant que `i < len(s)` :
  - [x] compter combien de fois `s[i]` se répète à la suite (`j` avance tant que `s[j] == s[i]`)
  - [x] ajouter le caractère à `rst`
  - [x] ajouter le nombre seulement si `count > 1`
  - [x] sauter de `count` cases : `i += count`
- [x] Renvoyer `rst`

## 3. Étapes — decompress
- [x] `rst = ""`, `i = 0`
- [x] Tant que `i < len(s)` :
  - [x] lire le caractère `c = s[i]`, puis `i += 1`
  - [x] lire TOUS les chiffres qui suivent dans `nb` (`s[i].isdigit()`)
  - [x] si `nb` est vide, ajouter `c` une fois, sinon ajouter `c * int(nb)`
- [x] Renvoyer `rst`

## 4. Outils Python
- `str(count)`, `int(nb)`, `s[i].isdigit()`
- `"a" * 3` donne `"aaa"`

## 5. Pièges
- Nombres à plusieurs chiffres : `"a12"` donne 12 `a`, donc il faut lire les chiffres en boucle, pas un seul
- Ne pas écrire `1` pour un caractère seul
- Vérifier `j < len(s)` AVANT `s[j]` (sinon IndexError)

## 6. Tests
| Entrée | Attendu |
|---|---|
| `compress("aabcccccaaa")` | `"a2bc5a3"` |
| `compress("")` | `""` |
| `compress("abc")` | `"abc"` |
| `compress("aaaaaaaaaaaa")` | `"a12"` |
| `decompress("a12")` | 12 × `a` |
