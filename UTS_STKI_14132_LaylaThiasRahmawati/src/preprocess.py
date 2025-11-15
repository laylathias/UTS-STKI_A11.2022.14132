import os, re
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

stop_words = set(stopwords.words('indonesian'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def tokenize(text):
    return text.split()

def remove_stopwords(tokens):
    return [t for t in tokens if t not in stop_words]

def stem(tokens):
    return [stemmer.stem(t) for t in tokens]

def preprocess(text):
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = stem(tokens)
    return tokens

def process_folder(raw_folder, out_folder):
    os.makedirs(out_folder, exist_ok=True)
    for fname in os.listdir(raw_folder):
        if fname.endswith(".txt"):
            with open(os.path.join(raw_folder, fname), "r", encoding="utf-8") as f:
                text = f.read()
            tokens = preprocess(text)
            with open(os.path.join(out_folder, fname), "w", encoding="utf-8") as f:
                f.write(" ".join(tokens))
    print("Preprocessing selesai.")