# Veritas Transcription Standard (VTS-v1)

Ce document définit le standard de transcription utilisé dans le projet **Veritas-Kernel**. Ce standard est optimisé pour le traitement par Intelligence Artificielle afin d'éliminer les collisions sémantiques entre les racines arabes.

## 1. La Distinction Fondamentale (أ vs ع)

Dans les transcriptions latines classiques, la lettre **أ** (Hamza/Alif) et la lettre **ع** ('Ain) sont souvent représentées par le caractère **A**. Dans le système Veritas, cela est considéré comme un **Bug de Collision**.

| Lettre Arabe | Signe Veritas | Rôle Systémique | Exemple |
| :--- | :--- | :--- | :--- |
| **أ** | **A** | Point d'entrée / Signal initial | `أ-ر-ض (A-R-D)` |
| **ع** | **'** | Profondeur / Action récursive | `ع-ز-ز ('-Z-Z)` |



## 2. Formatage des Entrées

Chaque racine dans le `LEXICON.json` suit une structure stricte :
`"ARABIC-ROOT (LATIN-ROOT/Transcription_Name)"`

### Règles :
- Les lettres de la racine latine sont séparées par des tirets `-`.
- Le `'` (Ain) est traité comme une consonne pleine.
- Le nom de transcription après le slash `/` doit porter le `'` s'il commence par un `ع`.

## 3. Pourquoi ce standard ?

Les IA (LLM) s'appuient sur la tokenisation. Si `Amr` (Commandement) et `'Amr` (Vie/Âge) sont écrits tous les deux `Amr`, l'IA perd le **Déterminisme**. 
Le standard **VTS-v1** garantit que :
1. Chaque jeton (token) possède une adresse unique dans le Lexicon.
2. L'IA peut remonter à la fonction logique (`logic_function`) sans ambiguïté.
3. La méthode **Ghayr dhi 'iwaj** est préservée au niveau du caractère.
