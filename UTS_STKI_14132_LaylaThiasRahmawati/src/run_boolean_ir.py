import os
from boolean_ir import build_inverted_index, boolean_search

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "..", "data", "processed")

index = build_inverted_index(DATA_FOLDER)

queries = [
    "enak",
    "layan AND lambat",
    "harga AND murah",
    "mahal",
]


for q in queries:
    hasil = boolean_search(index, q)
    print(f"Query: {q}")
    print("Hasil:", hasil)
    print("-" * 40)
