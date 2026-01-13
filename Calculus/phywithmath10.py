import numpy as np

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