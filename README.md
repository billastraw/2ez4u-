# 2EZ4U Food Delivery

Aplikasi **2EZ4U Food Delivery** merupakan aplikasi pengelolaan pesanan layanan pesan-antar makanan yang dikembangkan menggunakan Python. Aplikasi ini dibuat sebagai implementasi materi Struktur Data dan Algoritma (SDA).

Project ini dikembangkan secara bertahap melalui enam milestone, namun saat ini hanyalah laporan dari 3 milestone pertama (M1, M2, dan M3), yang mencakup pengelolaan data pesanan, pengelolaan antrean dan riwayat aksi, serta pengolahan dan pelaporan data pesanan.

## 1. Project Overview
Dalam layanan pesan-antar makanan, pengelolaan pesanan perlu dilakukan secara efisien agar data pelanggan, restoran, menu, harga, dan status pesanan dapat dikelola dengan baik. Melalui aplikasi 2EZ4U Food Delivery, konsep Struktur Data dan Algoritma diterapkan pada proses pengelolaan pesanan. Implementasi dilakukan menggunakan Python dengan antarmuka grafis berbasis Tkinter serta penyimpanan data menggunakan file CSV.

## 2. Features
Fitur utama aplikasi meliputi:
- Pembacaan dan penyimpanan data menggunakan file CSV.
- Pengelolaan data pesanan makanan.
- Penggunaan Array dan Linked List untuk menyimpan data pesanan.
- Pengelolaan antrean pesanan menggunakan struktur data Queue.
- Penggunaan Stack untuk mendukung operasi tertentu, termasuk riwayat atau yang disebut history.
- Pengelolaan pembatalan dan pengulangan aksi melalui Stack.
- Konversi ekspresi infix menjadi postfix dan evaluasi ekspresi postfix.
- Pengolahan data serta penyusunan laporan melalui modul M3.
- Antarmuka aplikasi berbasis Tkinter.
  
## 3. Milestone Implementation
### M1 — Order Data Management
M1 berfokus pada pengelolaan data pesanan menggunakan struktur data dasar.
Struktur data yang digunakan:
- Array: Menyimpan kumpulan data pesanan dalam susunan elemen yang dapat diakses berdasarkan indeks.
- Linked List: Menyimpan data dalam node yang saling terhubung sehingga penambahan dan penghapusan elemen dapat dilakukan melalui pengelolaan hubungan antarnode.

Modul M1 digunakan untuk mendukung pengelolaan data pesanan, termasuk pemuatan data dari CSV dan penyajian data kepada aplikasi.
File implementasi: `backend/m1_pesanan.py`

### M2 — Queue, Stack, and Expression Processing
M2 berfokus pada penerapan struktur data Stack dan Queue serta pengolahan ekspresi aritmetika.
Struktur data dan algoritma yang digunakan:
- Stack: Struktur data dengan prinsip LIFO (*Last In, First Out*), yaitu elemen terakhir yang masuk menjadi elemen pertama yang dikeluarkan.
- Naive Queue: Antrean dengan prinsip FIFO (*First In, First Out*).
- Circular Queue: Antrean yang memanfaatkan kembali ruang kosong pada penyimpanan secara melingkar.
- Undo and Redo: Mekanisme untuk membatalkan dan mengulangi aksi menggunakan Stack.
- Infix to Postfix Conversion: Konversi ekspresi aritmetika dari notasi infix menjadi postfix.
- Postfix Evaluation: Evaluasi ekspresi postfix menggunakan Stack.
  
File implementasi: `backend/m2_antrean.py`

### M3 — Data Processing and Reporting
M3 berfokus pada pengolahan data dan penyusunan laporan yang berkaitan dengan pesanan.
Sorting Algoritma:
- Insertion Sort: Mengurutkan data dengan menyisipkan elemen ke posisi yang tepat.
- Merge Sort: Mengurutkan data menggunakan pendekatan divide.
Pengurutan dapat dilakukan berdasarkan ID pesanan (oid), harga (harga), dan waktu penyelesaian (selesai).

Searching Algoritma:
- Linear Search: Mencari ID pesanan dengan memeriksa elemen satu per satu.
- Binary Search: Mencari ID pesanan dengan membagi area pencarian menjadi dua. Data harus terurut berdasarkan ID terlebih dahulu.

Modul ini juga menghitung jumlah perbandingan (comparison) dan pemindahan data (movement) untuk menganalisis kinerja algoritma.
File implementasi: `backend/m3_laporan.py`

## 4. Teknologi yang digunakan
1. Python 3.11 : Bahasa pemrograman
2. Tkinter : Pembuatan UI
   
## 5. Struktur Project Sejauh Ini
```text
2ez4u/
├── app.py
├── backend/
│   ├── m1_pesanan.py
│   ├── m2_antrean.py
│   └── m3_laporan.py
├── frontend/
│   └── ui.py
└── data/
    ├── pesanan.csv
    └── peta.csv
```

## 6. Screenshot
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/c68ccb70-4edb-412c-91c5-2384451e9af3" />
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/8d27c03c-f7db-426c-9bed-bd806a135a14" />
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/4d4cb046-54e8-42eb-92f0-2755d7ad9e82" />
<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/174e4c86-7bb6-4c95-afa8-ae2379c1ec3a" />

```

