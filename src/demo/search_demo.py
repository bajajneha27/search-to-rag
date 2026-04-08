import re
from collections import defaultdict

documents = {
    1: "Wireless mouse for laptop",
    2: "Gaming mouse with RGB lights",
    3: "Bluetooth keyboard and mouse combo",
    4: "Laptop stand for desk",
}

def tokenize(text):
    text = text.lower()
    return re.findall(r'\w+', text)

def build_index(docs):
    index = defaultdict(list)
    for doc_id, text in docs.items():
        tokens = tokenize(text)
        for token in tokens:
            index[token].append(doc_id)
    return index

def search(query, index):
    tokens = tokenize(query)

    if not tokens:
        return []

    results = set(index.get(tokens[0], []))

    for token in tokens[1:]:
        results &= set(index.get(token, []))

    return list(results)

def display_results(results):
    if not results:
        print("No results found\n")
        return
    for doc_id in results:
        print(f"{doc_id}: {documents[doc_id]}")
    print()

if __name__ == "__main__":
    index = build_index(documents)

    print("Simple Search Engine (type 'exit' to quit)\n")

    while True:
        query = input("Search: ")
        if query == "exit":
            break

        results = search(query, index)
        display_results(results)