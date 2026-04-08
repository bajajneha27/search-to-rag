
# The Inverted Index

Imagine a room full of books.

You are asked:
Find all books containing the word "mouse".

| Term      | Documents       |
|----------|----------------|
| wireless | 1              |
| mouse    | 1, 2, 3        |
| gaming   | 2              |
| bluetooth| 3              |

---

## Query: "wireless mouse"

- wireless → 1  
- mouse → 1, 2, 3  

Intersection → 1

---

## Terminology

- Term = word  
- Postings list = list of documents

---

## Query

wireless mouse

→ lookup both  
→ intersect results  
→ Doc1  

---

## Storage

- stored on disk  
- cached in memory for fast access  

---

## Data structures

- hash tables  
- B-trees  


----

<details>
<summary> Speaker Notes </summary>

- Start with: "Imagine we scan every document — too slow"
- Emphasize: "We precompute this structure"
- Walk through the table slowly
- Ask: "Which document contains both words?"
- Pause before saying "intersection"
</details>