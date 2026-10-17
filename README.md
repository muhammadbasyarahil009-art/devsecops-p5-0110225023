# DevSecOps P5 — Manajemen Data Mahasiswa

Implementasi pipeline DevSecOps menggunakan GitHub Actions untuk melakukan build, unit testing, dan Static Application Security Testing (SAST) pada aplikasi Python Manajemen Data Mahasiswa.

## Deskripsi Proyek

Aplikasi Manajemen Data Mahasiswa merupakan aplikasi berbasis Python yang digunakan untuk mengelola data mahasiswa melalui terminal. Proyek ini dikembangkan sebagai implementasi praktik DevSecOps dengan mengintegrasikan pengujian otomatis dan pemindaian keamanan kode ke dalam proses pengembangan perangkat lunak.

## Fitur Aplikasi

- Menambahkan data mahasiswa.
- Menampilkan data mahasiswa.
- Mencari data mahasiswa.
- Menghapus data mahasiswa.
- Menyimpan data mahasiswa ke file JSON.
- Membuat laporan data mahasiswa.

## Teknologi yang Digunakan

- Python 3
- Git dan GitHub
- GitHub Actions
- Pytest untuk unit testing
- Bandit untuk Static Application Security Testing (SAST)

## Struktur Proyek

```text
devsecops-p5-0110225023/
├── .github/
│   └── workflows/
│       └── devsecops.yml
├── tests/
│   └── test_mahasiswa.py
├── app.py
├── mahasiswa.py
├── validasi.py
├── penyimpanan.py
├── laporan.py
├── requirements.txt
├── README.md
└── data_mahasiswa.json
```

## Persyaratan

- Python 3.10 atau versi yang kompatibel dengan aplikasi.
- pip untuk menginstal dependensi.

## Cara Menjalankan Aplikasi

1. Clone repository:

   ```bash
   git clone https://github.com/muhammadbasyarahil009-art/devsecops-p5-0110225023.git
   ```

2. Masuk ke folder proyek:

   ```bash
   cd devsecops-p5-0110225023
   ```

3. Instal dependensi:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Jalankan aplikasi:

   ```bash
   python app.py
   ```

## Pengujian Otomatis

Unit test dijalankan untuk memeriksa fungsi aplikasi agar bekerja sesuai harapan.

```bash
python -m pytest -v
```

## Static Application Security Testing (SAST)

Pemindaian keamanan kode dilakukan menggunakan Bandit untuk mendeteksi pola kode Python yang berpotensi memiliki kerentanan keamanan.

Perintah pemindaian lokal:

```bash
python -m bandit -r . -x ./tests
```

## Pipeline GitHub Actions

Pipeline otomatis dijalankan ketika terdapat push ke branch `main` atau pull request.

Pipeline terdiri dari dua job utama:

1. **Build and Unit Test** — menyiapkan Python, menginstal dependensi, dan menjalankan unit test.
2. **SAST Security Scan** — menjalankan Bandit untuk memindai potensi kerentanan keamanan pada kode Python.

Hasil eksekusi pipeline dapat dilihat melalui tab **Actions** pada repository GitHub.

## Identitas Proyek

- Repository: `devsecops-p5-0110225023`
- Platform: GitHub
- Fokus: Implementasi CI dan SAST menggunakan GitHub Actions.

## Lisensi

Proyek ini dibuat untuk keperluan pembelajaran dan tugas praktikum DevSecOps.
