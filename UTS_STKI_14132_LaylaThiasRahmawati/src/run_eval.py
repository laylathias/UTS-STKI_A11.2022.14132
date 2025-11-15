from vsm_ir import load_docs, compute_tfidf, search_vsm
from eval_ir import precision_at_k, recall, f1_score, average_precision, map_k

DOC_FOLDER = r"D:\Semester 7\STKI\UTS_STKI_14132\data\processed"

# 1. Load dokumen
docs = load_docs(DOC_FOLDER)
tfidf_docs, idf = compute_tfidf(docs)

# 2. Buat 3 query + gold standard manual
queries = {
    "enak": {"doc01.txt", "doc05.txt"},
    "layan lambat": {"doc03.txt"},
    "harga murah": {"doc10.txt"}
}

retrieved = {}

# 3. Jalankan pencarian
for q in queries:
    results = search_vsm(q, tfidf_docs, idf, topk=5)
    doc_list = [doc for doc, score in results]
    retrieved[q] = doc_list

    print("\n===================================")
    print("Query:", q)
    print("Retrieved:", doc_list)
    print("Relevant:", queries[q])

    p5 = precision_at_k(doc_list, queries[q], k=5)
    r = recall(doc_list, queries[q])
    ap = average_precision(doc_list, queries[q])

    print(f"Precision@5 = {p5:.3f}")
    print(f"Recall      = {r:.3f}")
    print(f"Avg Precision = {ap:.3f}")

# 4. Hitung MAP
m = map_k(retrieved, queries)
print("\nMAP =", round(m, 3))
