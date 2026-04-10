
# Indexing

This is the "heavy lifting" part of the process where we turn messy, unstructured text into a highly organized, searchable data structure.

Think of indexing as creating the Inverted Index. While a normal index (like a table of contents) tells you what is in a chapter, an inverted index tells you which "chapters" (documents) contain a specific word.

Let's take a small document for example:

`Introduction to Programming with Python`

---

## Step 1: Tokenization & Normalization

`["introduction", "to", "programming", "with", "python" ]`

## Step 2: Stop-word Removal

`["introduction", "programming", "python"]`

## Step 3: Stemming / Lemmatization

`["introduce", "program", "python"]`

---

Some other transformation techniques that can be considered are:

- Handling punctuations: `Python!` --> `python`
- Handling abbreviations: `AI` --> `Artificial Intelligence`
- Synonym Expansion: `laptop` --> `[computer, notebook]`
- De-compounding: `smartphone` --> `[smart, phone]`
- N-grams: `python` --> `[pyt, yth, tho, hon]`