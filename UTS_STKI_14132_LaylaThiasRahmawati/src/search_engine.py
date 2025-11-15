# search_engine.py
from boolean_ir import build_inverted_index, boolean_search
from vsm_ir import load_docs, compute_tfidf, search_vsm

PROCESSED_FOLDER = r"D:\Semester 7\STKI\UTS_STKI_14132_LaylaThiasRahmawati\data\processed"

# --- Boolean ---
index = build_inverted_index(PROCESSED_FOLDER)

def search_boolean(query):
    return boolean_search(index, query)


# --- VSM ---
docs = load_docs(PROCESSED_FOLDER)
tfidf_docs, idf = compute_tfidf(docs)

def search_vsm_mode(query):
    return search_vsm(query, tfidf_docs, idf, topk=5)
