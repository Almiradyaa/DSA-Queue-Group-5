# DSA-Queue-Group-5
Repository ini dibuat untuk memenuhi tugas mata kuliah Algoritma dan Struktur Data. Repository ini berisi solusi dari practice problem berjudul Stone Pile, yang diambil dari web CodeChef. Dalam masalah ini, konsep struktur data Queue diterapkan untuk menyelesaikan tantangan yang diberikan.
#### Nama: Dita Ayodya Al Mira
#### NIM: D121241008
#### Problem Link: [Stone Pile - CodeChef](https://www.codechef.com/practice/course/stacks-and-queues/STAQUEF/problems/STONE_PILE)  
#### Difficulty: 1200 (Easy to Medium)
# Short Approach Summary
## Pemahaman Masalah
Permainan dimulai dengan sejumlah batu yang diberi angka. Dua pemain, Aman dan Akshat, secara bergiliran mengambil giliran dengan aturan:
* Aman: melakukan 1 kali rotasi (memindahkan elemen paling depan ke belakang), lalu membuang elemen paling depan.
* Akshat: melakukan 2 kali rotasi (dua kali memindahkan elemen depan ke belakang), lalu membuang elemen paling depan.

Permainan berlanjut hingga hanya tersisa satu batu, dan program harus menentukan siapa pemain terakhir yang melakukan aksi, serta angka batu yang tersisa.

## Struktur Data yang Digunakan: collections.deque
Untuk menyelesaikan simulasi ini secara efisien, digunakan struktur data deque (double-ended queue) dari modul collections di Python. Beberapa alasan penggunaannya:
* deque memungkinkan operasi pembuangan dan penambahan elemen dari kedua ujung secara efisien (kompleksitas waktu O(1)).
*	Operasi seperti popleft() dan append() sangat cocok untuk mensimulasikan rotasi dan pembuangan pada antrian.

## Langkah Penyelesaian
1.	Input Data: Program menerima beberapa test case. Setiap test case terdiri dari jumlah batu dan daftar angka batunya.
2.	Inisialisasi deque: Angka-angka batu diubah menjadi queue (deque) untuk memulai simulasi.
3.	Simulasi Giliran Pemain:
    * Aman (giliran ganjil): 1x rotasi + 1x buang
    * Akshat (giliran genap): 2x rotasi + 1x buang
4.	Penghentian: Simulasi berhenti saat panjang deque tinggal 1. Pemain terakhir dan batu terakhir dicatat.
5.	Output Hasil: Ditampilkan dalam bentuk nama pemain terakhir dan angka batu yang tersisa.
   
## Fokus Pembelajaran
* Mengenal deque sebagai bentuk implementasi antrian dua arah di Python.
* Mempelajari simulasi berbasis antrian dan pergantian giliran.
* Menyusun logika program yang mencerminkan aturan permainan dengan jelas.
* Memodifikasi tampilan penerimaan input agar lebih interaktif.

