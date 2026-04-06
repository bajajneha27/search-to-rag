
# Handling Typos: Fuzzy Search

What happens if the query has a typo?

Example:
- wirless mause

---

## Problem

Exact matching fails:
- "wirless" ≠ "wireless"

---

## Solution: Fuzzy Matching

Instead of exact match:
- find similar words

---

## Idea (intuition)

- small spelling differences are allowed
- system suggests closest valid term

---

## Example

```mermaid
graph LR
    A["wirless"] --> B["Did you mean: wireless"]
    B --> C["Results"]

### Speaker Notes

- Ask: "Have you ever mistyped a query?"
- Show failure first
- Then say: "Search systems are forgiving"
- Keep it intuitive, avoid algorithm details