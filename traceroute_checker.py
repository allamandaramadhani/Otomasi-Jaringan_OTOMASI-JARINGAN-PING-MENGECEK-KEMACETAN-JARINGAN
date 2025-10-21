import os
import platform
import re

# === Konfigurasi target ===
target = "8.8.8.8"  # bisa kamu ganti ke IP lain, misal: 172.16.45.35
print(f"🔍 Mengecek jalur koneksi (traceroute) ke {target}...\n")

# === Tentukan perintah traceroute sesuai OS ===
system_os = platform.system().lower()

if "windows" in system_os:
    command = f"tracert {target}"
else:
    # versi traceroute untuk Linux DevNet (tanpa -n)
    command = f"traceroute {target}"

# === Jalankan traceroute ===
result = os.popen(command).read()
print("=== HASIL TRACEROUTE ===")
print(result)

# === Analisis hasil traceroute ===
print("=== ANALISIS ===")

# Ambil waktu dari hasil traceroute (ms)
times = re.findall(r"(\d+\.\d+)\s*ms", result)

if not times:
    print("❌ Tidak dapat membaca waktu respon. Periksa koneksi atau izin admin.")
else:
    times = list(map(float, times))
    avg_time = sum(times) / len(times)
    max_time = max(times)
    min_time = min(times)

    print(f"📊 Jumlah hop terdeteksi: {len(times)}")
    print(f"⏱️ Waktu tercepat: {min_time:.2f} ms")
    print(f"🐢 Waktu terlambat: {max_time:.2f} ms")
    print(f"📈 Rata-rata waktu: {avg_time:.2f} ms")

    # Deteksi kemacetan
    if max_time - min_time > 100:
        print("⚠️ Terdapat kemacetan jaringan pada beberapa hop (delay tinggi).")
    else:
        print("✅ Jalur koneksi stabil, tidak ada kemacetan signifikan.")
