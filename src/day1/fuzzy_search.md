
# Fuzzy Search & Tolerant Retrieval

Fuzzy search is the "forgiveness" layer of a search engine. It ensures that typos, phonetic misspellings, or variations don't result in an empty "0 results found" page.

## Edit Distance (Levenshtein Distance)

This algo treats words as strings of characters and calculates the "cost" to transform one into another. The lower the cost, the more likely it's a match.

- **Insertion**: Add a character (e.g., pyton --> python).
- **Deletion**: Remove a character (e.g., pythhon --> python).
- **Substitution**: Swap a character (e.g., pythun --> python).

## K-grams (N-grams)

K-grams break words into overlapping chunks of length `k`.

If we use 3-grams (trigrams) for the term `python`, we get:
`#py`, `pyt`, `yth`, `tho`, `hon`, `on#` (where `#` marks the start/end).

Example: User types `pythun`

- **"python" grams**: pyt, yth, tho, hon
- **"pythun" grams**: pyt, yth, thu, hun

## Other Fuzzy Techniques

- **Phonetic Algorithms**: (e.g., Soundex or Metaphone) Matching words that sound the same but are spelled differently, like "Smith" and "Smyth."
- **Transposition**: Specifically handling when two letters are swapped (e.g., `pythno` --> `python`), which is a very common human typo.
- **SymSpell**: A very fast algorithm that uses pre-calculated deletions to find matches in milliseconds.
