from vsm_ir import load_docs, compute_tfidf, search_vsm

DOC_FOLDER = r"D:\Semester 7\STKI\UTS_STKI_14132\data\processed"

docs = load_docs(DOC_FOLDER)
tfidf_docs, idf = compute_tfidf(docs)

queries = [
    "enak",
    "layan cepat",
    "harga murah",
    "lambat pelayanan"
]

for q in queries:
    print("\nQuery:", q)
    results = search_vsm(q, tfidf_docs, idf, topk=5)
    for doc, score in results:
        print(f"  {doc}  --> {score:.4f}")
