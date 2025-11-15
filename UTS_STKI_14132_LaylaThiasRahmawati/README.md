**NAMA**: LAYLA THIAS RAHMAWATI
**NIM**: A11.2022.14132
**MATA KULIAH**: Sistem Temu Kembali Informasi
**TOPIK UTS**: Sistem Temu Kembali Informasi pada Review Restoran Menggunakan Boolean Retrieval dan Vector Space Model

**DESKRIPSI PROJECT**
Project ini membangun sebuah sistem temu kembali informasi (IR) sederhana menggunakan dataset 10 review restoran dalam bentuk file teks. Sistem ini melakukan preprocessing teks, membangun index, melakukan pencarian menggunakan dua model IR (Boolean dan VSM), memberikan ranking dokumen, melakukan evaluasi, dan diakhiri dengan implementasi search engine mini.

Sistem ini bekerja dengan menerima kata kunci dari pengguna, misalnya “enak ramah”, kemudian membersihkan dan memproses query tersebut agar sesuai dengan format dokumen yang sudah dipreprocessing. Setelah itu, sistem membandingkan query dengan seluruh review restoran menggunakan dua pendekatan. Pada model Boolean Retrieval, sistem mencari dokumen yang benar-benar mengandung semua kata dalam query. Sementara pada Vector Space Model (VSM), sistem menghitung tingkat kemiripan antara isi dokumen dan query menggunakan TF-IDF dan cosine similarity, sehingga dokumen yang tidak mengandung kata secara persis tetap bisa diberi skor relevansi. Hasil pencarian kemudian ditampilkan dalam dua bentuk: Boolean memberikan hasil cocok/tidak cocok, sedangkan VSM menampilkan daftar dokumen yang diurutkan berdasarkan tingkat kemiripan tertinggi. Dengan cara ini, sistem mampu membantu pengguna menemukan review restoran yang paling relevan dengan pencarian mereka.

Tools dan library yang digunakan adalah: Python 3, NLTK, Sastrawi, NumPy / math, dan VSCode

**TUJUAN EKSPERIMEN**
1. Mengolah data teks tidak terstruktur.
2. Membuat inverted index untuk Boolean Retrieval.
3. Menghitung TF, DF, IDF, TF-IDF, dan cosine similarity.
4. Menghasilkan ranking dokumen berdasarkan relevansi.
5. Mengukur performa IR menggunakan Precision–Recall–AP–MAP.
6. Menggabungkan Boolean dan VSM dalam satu mini search engine.

**ALUR SISTEM**
1. Input Dokumen (.txt)
Dokumen review diletakkan di folder data/raw/.

2. Preprocessing
Lowercase
Cleaning
Tokenizing
Stopword removal
Stemming (Sastrawi)

3. Indexing
Inverted index → Boolean retrieval
TF-IDF index → VSM ranking

4. Query Processing
Query utama contoh: "enak ramah"


5. Retrieval Process
Boolean → cocok atau tidak
VSM → nilai similarity

6. Ranking (khusus VSM)
Hasil diurutkan berdasarkan skor tertinggi.

7. Evaluasi Model IR
Precision@k, Recall, AP, MAP.

8. Search Engine Mini
Integrasi Boolean + VSM.

**STRUKTUR FOLDER PROJECT**
UTS_STKI_14132_LaylaThiasRahmawati/
│
├── data/
│   ├── raw/       
│   └── processed/    
│
├── src/
│   ├── boolean_ir.py
│   ├── debug_print.py
│   ├── eval_ir.py
│   ├── eval.py
│   ├── preprocess.py
│   ├── run_boolean_ir.py
│   ├── run_eval.py
│   ├── run_preprocess.py
│   ├── run_vsm.py
│   ├── search_engine.py
│   ├── test_nltk.py
│   ├── vsm_ir.py
│   ├── run_eval.py
│   └── _pycache_/
│
├── notebooks/
│   └── UTS_STKI_14132_LaylaThiasRahmawati.ipynb
│
├── Laporan.pdf
│
└── README.md
