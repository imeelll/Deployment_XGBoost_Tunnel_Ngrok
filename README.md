## Fraud Detection Web Application with XGBoost and Streamlit
Aplikasi web interaktif untuk mendeteksi transaksi penipuan (fraud) menggunakan model XGBoost yang telah dilatih sebelumnya. Dibangun menggunakan Streamlit untuk antarmuka pengguna dan dilengkapi fitur tunneling dengan Ngrok agar aplikasi dapat diakses dari publik tanpa konfigurasi server yang rumit.

## Fitur Utama
- Input data transaksi berupa merchant, kategori, jumlah transaksi, lokasi, waktu, gender, dan nomor kartu kredit (di-hash untuk keamanan).
- Perhitungan jarak geografis antara lokasi transaksi dan merchant menggunakan rumus Haversine via library geopy.
- Pengolahan data kategorikal dengan Label Encoding, lengkap dengan penanganan kasus label yang tidak pernah muncul saat pelatihan.
- Prediksi langsung menggunakan model XGBoost untuk menentukan apakah transaksi termasuk fraud atau legitimate.
- Tersedia URL publik aplikasi dengan bantuan Ngrok tunnel.

## Struktur Folder dan File Penting
- app.py – Script utama aplikasi Streamlit yang memuat logika input, preprocessing, dan prediksi.
- fraud_detection_model.jb – Model XGBoost hasil pelatihan yang disimpan menggunakan joblib.
- label_encoder.jb – Dictionary encoder berisi LabelEncoder untuk kolom-kolom kategorikal.
- deploy_tunnel_ngrok.py (opsional) – Script untuk menjalankan Ngrok dan meng-expose aplikasi ke internet.
- requirements.txt – Daftar dependensi Python yang dibutuhkan.

## Prasyarat
- Python 3.7 atau versi lebih baru.
- Paket Python yang terdaftar di requirements.txt.
- Akun Ngrok (untuk penggunaan tunneling publik dengan batas tertentu).

## Panduan Instalasi dan Penggunaan
1. Clone atau download repository:

git clone [URL_REPOSITORY_ANDA]
cd [NAMA_FOLDER_PROJECT]

2. Buat dan aktifkan virtual environment (opsional tapi disarankan):

python -m venv venv
Aktifkan environment:
Windows (cmd): .\venv\Scripts\activate
macOS/Linux: source venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Jalankan aplikasi Streamlit:

streamlit run app.py

5. (Opsional) Jalankan deploy_tunnel_ngrok.py untuk mendapatkan URL publik:

python deploy_tunnel_ngrok.py

## Cara Menggunakan
- Buka aplikasi di browser menggunakan URL lokal (biasanya http://localhost:8501).
- Masukkan data transaksi pada form yang disediakan.
- Tekan tombol Predict untuk mendapatkan prediksi transaksi fraud atau legitimate.
- Jika menggunakan ngrok, akses aplikasi melalui URL publik yang disediakan.

## Catatan
- Label Encoding di-handle dengan hati-hati agar aplikasi tidak error saat input kategori baru.
- Nomor kartu kredit diproses dengan hashing untuk menjaga kerahasiaan data.
- Ngrok free tier membatasi jumlah tunnel aktif, pastikan mematikan tunnel lama sebelum membuka yang baru.

## Tim Pengembang
Amelia Rahmadani
M. Zacky

