
# Demo: A Simple Search

Let’s start with a simple search system:

We have a small collection of documents:

- Doc1: wireless mouse for laptop  
- Doc2: gaming mouse with RGB  
- Doc3: bluetooth presentation pointer  
- Doc4: budget office mouse  

---

### Try: "wireless mouse"

We get Doc1.  
This works because both words are present.

---

### Try: "mouse"

We get multiple documents.  
This works because more documents contain the word "mouse".

---

### Try: "laptop mouse"

We only get documents containing both words.  
This system performs an AND operation.

---

### Try: "wirless mouse"

No results.

Even though the intent is clear, the system fails due to exact matching.

---

### Try: "device for presentations"

No results again.

Even though Doc3 is relevant.

---

Let’s now understand what’s happening internally.