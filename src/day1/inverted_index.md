
# The Inverted Index

Documents collection:

- Doc1: "Introduction to Programming with Python"
- Doc2: "Advanced Programmers Handbook"
- Doc3: "The History of Computer Programs"
- Doc4: "A Guide to Gardening in the Spring"

### Mapping Terms to Documents

| Term       | Documents      |
|------------|----------------|
| `introduc` | 1              |
| `program`  | 1, 2, 3        |
| `python`   | 1              |
| `advanc`   | 2              |
| `handbook` | 2              |
| `histori`  | 3              |
| `comput`   | 3              |
| `garden`   | 4              |
| `spring`   | 4              |

---

### Core Concepts
An inverted index is made of two main parts:

- **The Dictionary**: A list of all unique terms (stems) in the collection.
- **The Postings List**: The actual lists of document IDs associated with those terms.

### Data Structures for Dictionary:

- **Hash Tables**: Provide $O(1)$ lookup time. Great for exact matches, but they don't support "starts with" or range searches.
- **B Trees**: Most common in production databases (like PostgreSQL). They keep terms sorted, which is essential for searching for things like comput* to find both "computer" and "computing."
- **Tries (Prefix Trees)**: Extremely efficient for storing overlapping prefixes (like apple, apply, applied).

### Storing the Postings (The "Postings List")

- **Linked Lists vs. Arrays**: We usually use Variable-length Arrays. They are more cache-friendly than linked lists and allow for faster "jumping" during intersection math.
- **Compression (Delta Encoding)**: Instead of storing IDs like [102, 105, 110], we store the gaps: [102, 3, 5]. Smaller numbers take up fewer bits, significantly reducing the index size on disk.