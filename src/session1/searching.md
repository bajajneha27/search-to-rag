# Query Processing

When a user hits "Enter" on a search. That's when the query processing phase starts.

Let's process the query:

"Best books for programming in Python"

---

## The Workflow

- **Parsing**: Breaking the query string into parts.
- **Transformation**: Applying the exact same pipeline (Normalization → Stop-words → Stemming).
Result : `[book, program, python]`
- **Speling Correction**:
    - Edit Distance
    - K-gram Indexing
- **Lookup**: Finding the terms in our Inverted Index.
- **Merging/Logic**: Combining results (AND, OR, NOT).
- **Ranking**: Sorting the results so the "best" one is at the top.
    - **Term Frequency (TF)**:

    \\(TF(t, d) = \frac{\text{Number of times term } t \text{ appears in document } d}{\text{Total number of terms in document } d}\\)

    - **Inverse Document Frequency (IDF)**:

    \\(IDF(t, D) = \log\left(\frac{\text{Total number of documents } N}{\text{Number of documents containing term } t}\right)\\)
