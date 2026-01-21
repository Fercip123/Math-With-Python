import numpy as np
"""
AI Curiosity-Driven Learning System
This module simulates an AI system that generates curiosity-driven learning branches
based on its current knowledge level of different topics.
The system maintains a knowledge dictionary tracking AI understanding (0-1 scale) and
dynamically creates new learning branches when curiosity is high (i.e., when knowledge
is low).
Functions:
    rasa_ingin_tahu(topik, data_baru): Analyzes a topic and generates new learning
        branches if the curiosity score (inverse of knowledge level) exceeds threshold.
Example:
    >>> pengetahuan_ai = {"angka": 0.95, "hewan": 0.10}
    >>> cabang_baru = rasa_ingin_tahu("hewan", "Data Kucing")
    >>> print(cabang_baru)
    ['Jenis-jenis hewan', 'Habitat hewan', 'Cara makan hewan']
"""
# and passes "Data Kucing" (cat data) as new information. The function calculates
# curiosity based on low knowledge (0.10) and returns a list of new learning branches.

# Pengetahuan AI saat ini (Skala 0 sampai 1)
pengetahuan_ai = {
    "angka": 0.95,  # Sudah sangat paham
    "hewan": 0.10,  # Hampir tidak tahu (Baru diberikan satu data)
}

def rasa_ingin_tahu(topik, data_baru):
    # Hitung seberapa besar "kejutan" (Surprise/Error)
    # Jika pengetahuan rendah, rasa ingin tahu (curiosity) tinggi
    curiosity_score = 1.0 - pengetahuan_ai[topik]
    
    print(f"Menganalisis topik: {topik}")
    print(f"Skor Rasa Ingin Tahu: {curiosity_score:.2f}")
    
    if curiosity_score > 0.5:
        print(">>> 'Aku penasaran! Mari buat percabangan baru.'")
        percabangan = ["Jenis-jenis " + topik, "Habitat " + topik, "Cara makan " + topik]
        return percabangan
    else:
        return "Aku sudah cukup paham ini."

# Simulasi saat kita beri data "Hewan"
cabang_baru = rasa_ingin_tahu("hewan", "Data Kucing")
print(f"Percabangan yang tercipta: {cabang_baru}")

