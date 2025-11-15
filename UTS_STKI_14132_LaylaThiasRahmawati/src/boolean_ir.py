import os

# Membuat inverted index dari folder data/processed
def build_inverted_index(folder):
    index = {}

    for fname in sorted(os.listdir(folder)):
        if not fname.endswith(".txt"):
            continue

        path = os.path.join(folder, fname)
        with open(path, "r", encoding="utf-8") as f:
            words = f.read().split()

        unique_words = set(words)
        for word in unique_words:
            if word not in index:
                index[word] = set()
            index[word].add(fname)

    return index

# Parsing query boolean sederhana
def parse_query(q):
    return q.lower().split()

# Operasi Boolean: AND, OR, NOT
def boolean_search(index, query):
    tokens = parse_query(query)

    if not tokens:
        return set()

    # Mulai dari term pertama
    result = index.get(tokens[0], set()).copy()

    i = 1
    while i < len(tokens) - 1:
        operator = tokens[i]
        term = tokens[i + 1]
        postings = index.get(term, set())

        if operator == "and":
            result = result & postings

        elif operator == "or":
            result = result | postings

        elif operator == "not":
            result = result - postings

        i += 2

    return result
