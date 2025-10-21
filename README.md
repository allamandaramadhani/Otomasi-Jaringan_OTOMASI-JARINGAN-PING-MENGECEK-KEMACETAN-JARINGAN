# Otomasi-Jaringan_OTOMASI-JARINGAN-PING-MENGECEK-KEMACETAN-JARINGAN
Script Python untuk automasi traceroute dan analisis jalur jaringan. Melakukan tracing rute ke IP target, menghitung statistik latency (min, max, rata-rata), dan mendeteksi kemacetan jaringan. Kompatibel dengan Windows dan Linux.


## 🧾 Deskripsi Proyek

Proyek ini dibuat untuk membantu dalam memahami bagaimana paket data melewati beberapa router (hop) untuk mencapai tujuan akhir di jaringan.  
Dengan melakukan analisis terhadap hasil traceroute, pengguna dapat mengetahui:
- Jumlah hop yang dilalui,
- Waktu tercepat, terlambat, dan rata-rata tiap hop,
- Adanya potensi **kemacetan jaringan (network congestion)**.

Program ini sangat berguna untuk:
- Praktikum jaringan komputer,
- Troubleshooting koneksi antar server,
- Analisis performa routing di jaringan lokal maupun internet.

---

## ⚙️ Fitur Utama
✅ Mendukung **Windows** dan **Linux (DevNet)**  
✅ Menjalankan perintah traceroute otomatis  
✅ Menampilkan hasil traceroute langsung di terminal  
✅ Menganalisis:
- Jumlah hop (lompatan jaringan)
- Waktu tercepat, terlambat, dan rata-rata
- Deteksi kemacetan jaringan  
✅ Menampilkan hasil dengan format dan emoji agar mudah dibaca  

---

## 🧠 Cara Menggunakan

### 1️⃣ Prasyarat
Pastikan kamu sudah memiliki:
- **Python 3**
- Akses **Command Prompt (Windows)** atau **Terminal (Linux)**

selanjutnya
1. Buat file bernama: traceroute_checker.py
2. simpan program lalu jalankan dengan script: python traceroute_checker.py


## hasil outputny ##
🔍 Mengecek jalur koneksi (traceroute) ke 8.8.8.8...

=== HASIL TRACEROUTE ===
traceroute to 8.8.8.8 (8.8.8.8), 30 hops max
 1  192.168.1.1 (192.168.1.1)  1.5 ms
 2  10.0.0.1 (10.0.0.1)  5.3 ms
 3  8.8.8.8 (8.8.8.8)  20.2 ms

=== ANALISIS ===
📊 Jumlah hop terdeteksi: 3
⏱️ Waktu tercepat: 1.50 ms
🐢 Waktu terlambat: 20.20 ms
📈 Rata-rata waktu: 9.00 ms
✅ Jalur koneksi stabil, tidak ada kemacetan signifikan.
