import os
import math
from collections import Counter

# Load dokumen yang sudah diproses
def load_docs(folder):
    docs = {}
    for fname in sorted(os.listdir(folder)):
        if fname.endswith(".txt"):
            with open(os.path.join(folder, fname), "r", encoding="utf-8") as f:
                tokens = f.read().split()
            docs[fname] = tokens
    return docs

# Hitung TF (term frequency)
def compute_tf(docs):
    tf = {}
    for doc, tokens in docs.items():
        tf[doc] = Counter(tokens)
    return tf

# Hitung DF (document frequency)
def compute_df(docs):
    df = Counter()
    for tokens in docs.values():
        for term in set(tokens):
            df[term] += 1
    return df

# IDF
def compute_idf(df, N):
    idf = {}
    for term, freq in df.items():
        idf[term] = math.log(N / freq)
    return idf

# TF-IDF docs
def compute_tfidf(docs):
    N = len(docs)
    tf = compute_tf(docs)
    df = compute_df(docs)
    idf = compute_idf(df, N)

    tfidf = {}
    for doc, counter in tf.items():
        weights = {}
        for term, count in counter.items():
            weights[term] = count * idf[term]
        tfidf[doc] = weights
    return tfidf, idf

# Bangun vector query (tanpa stemming)
def build_query_vector(query, idf):
    terms = query.lower().split()
    tf = Counter(terms)
    qvec = {}

    for term, count in tf.items():
        if term in idf:
            qvec[term] = count * idf[term]
    return qvec

# Cosine similarity
def cosine_similarity(vec1, vec2):
    common = set(vec1.keys()) & set(vec2.keys())
    dot = sum(vec1[t] * vec2[t] for t in common)

    mag1 = math.sqrt(sum(v * v for v in vec1.values()))
    mag2 = math.sqrt(sum(v * v for v in vec2.values()))

    if mag1 == 0 or mag2 == 0:
        return 0.0

    return dot / (mag1 * mag2)

# Ranking dokumen berdasarkan cosine
def search_vsm(query, tfidf_docs, idf, topk=5):
    qvec = build_query_vector(query, idf)

    scores = []
    for doc, dvec in tfidf_docs.items():
        score = cosine_similarity(qvec, dvec)
        scores.append((doc, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:topk]
