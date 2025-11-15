import os

folder = r"D:\Semester 7\STKI\UTS_STKI_14132_LaylaThiasRahmawati\data\processed"

for fname in sorted(os.listdir(folder)):
    with open(os.path.join(folder, fname), "r", encoding="utf-8") as f:
        print(fname, ":", f.read())
