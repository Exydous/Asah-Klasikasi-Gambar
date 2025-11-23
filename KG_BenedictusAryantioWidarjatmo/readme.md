# Proyek Klasifikasi Gambar (Image Classification)

Repository ini berisi submission proyek machine learning untuk klasifikasi gambar. Proyek ini mencakup kode pelatihan (training), evaluasi, serta model yang telah dikonversi ke berbagai format (SavedModel, TF Lite, dan TFJS) untuk kebutuhan deployment.

## 👤 Informasi Pembuat
* **Nama:** Benedictus Aryantio Widarjatmo
* **Email:** benedictusaryantiow@gmail.com
* **ID Dicoding:** M297D5Y0356

---

Struktur File

KG_BenedictusAryantioWidarjatmo
├───fruits_final_split                  # Dataset hasil split (Train, Val, Test)
    ├───test     
    ├───train
    ├───val
├───fruits_selected                     # Dataset yang sudah difilter (40 kelas terpilih)
    ├───Apple 5
    ├───Apple 6
    ├───Apple 7
    ├───Apple 8
    ├───..........
    ├───..........
    ├───..........        
├───fruits-360                          # Dataset mentah (sumber awal)
    ├───Test
    ├───Training             
├───saved_model                         # Model format TensorFlow SavedModel (.pb)
    ├───assets
    ├───variables
    ├───fingerprint.pb
    ├───saved_model.pb             
├───tfjs_model                          # Model hasil konversi ke TensorFlow.js (Web)
    ├───group1-shard1of7.bin
    ├───group1-shard2of7.bin     
    ├───group1-shard3of7.bin
    ├───group1-shard4of7.bin
    ├───group1-shard5of7.bin
    ├───group1-shard6of7.bin
    ├───group1-shard7of7.bin
    ├──model.json
├───tflite                              # Model hasil konversi ke TF Lite (Mobile/IoT)
    ├──label.txt
    ├──model.tflite           
├───notebook.ipynb                      # Source code utama (Jupyter Notebook)
├───readme.md                           # Dokumentasi proyek ini
└───requirement                         # Daftar library/dependencies (requirements.txt)# Asah-Klasikasi-Gambar
# Asah-Klasikasi-Gambar
