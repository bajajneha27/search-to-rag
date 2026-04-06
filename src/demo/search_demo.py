documents = {
  1: "wireless mouse for laptop",
  2: "gaming mouse wired",
  3: "bluetooth keyboard and mouse",
}

def search(query):
  terms = query.lower().split()
  results = []

  for doc_id, text in documents.items():
    if all(term in text for term in terms):
      results.append((doc_id, text))

  return results


if __name__ == "__main__":
  while True:
    q = input("Search: ")
    print(search(q))