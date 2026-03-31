# Tugas Python AI — B10

**Firman Fadilah** — 2308561037  
Informatika, Universitas Udayana  
AI Development B10 — Infinite Learning

---

## Daftar Tugas

| File        | Topik                  | Deskripsi                                                      |
| ----------- | ---------------------- | -------------------------------------------------------------- |
| `tugas3.py` | Dasar Python           | Variabel, tipe data, string, operasi matematika, list, input   |
| `tugas4.py` | Data Structures        | List, tuple, set, dictionary, nested structures, comprehension |
| `tugas5.py` | Function & Class       | Function dengan type hints, class Student, method, `__str__`   |
| `tugas6.py` | Modules, File I/O, OOP | NumPy, pandas DataFrame, file output, class GradeBook          |

---

## Kesimpulan

### Tugas 4 — Python Data Structures

Tugas ini membahas struktur data bawaan Python yang menjadi fondasi dalam pengolahan data. Dari tugas ini saya memahami perbedaan karakteristik masing-masing struktur: **list** bersifat mutable dan ordered sehingga cocok untuk koleksi data yang perlu dimanipulasi, **tuple** bersifat immutable sehingga cocok untuk data yang tidak boleh berubah, **set** secara otomatis menghilangkan duplikat dan mendukung operasi himpunan (union, intersection, difference), dan **dictionary** menyimpan data dalam pasangan key-value yang efisien untuk pencarian.

Bagian yang paling berguna adalah **nested structures** dan **comprehension**. Nested structure (list berisi dictionary) merepresentasikan data dunia nyata seperti daftar mahasiswa atau katalog produk. Comprehension membuat kode lebih ringkas dan Pythonic dibanding loop biasa — misalnya memfilter data atau mentransformasi elemen dalam satu baris.

### Tugas 5 — Function and Class

Tugas ini memperkenalkan dua konsep penting dalam pemrograman: **function** untuk modularitas kode dan **class** untuk pemrograman berorientasi objek (OOP). Dengan function, kode yang sering dipakai cukup ditulis sekali dan dipanggil berulang kali. Parameter default (`b: float = 0.0`) membuat function lebih fleksibel tanpa memaksa pemanggil mengisi semua argumen.

Class `Student` menunjukkan bagaimana OOP mengorganisasi data dan perilaku dalam satu entitas. Atribut menyimpan state (nama, nim, nilai) dan method mengoperasikan state tersebut (tambah nilai, hitung rata-rata, cek status). Method `__str__` membuat objek bisa langsung di-print dengan format yang rapi. Prinsip ini menjadi dasar untuk membangun aplikasi yang lebih kompleks di mana setiap komponen memiliki tanggung jawab yang jelas.

### Tugas 6 — Modules, File I/O, & OOP

Tugas ini mengintegrasikan library eksternal (NumPy dan pandas) dengan OOP dan file I/O. **NumPy** mempermudah komputasi statistik pada array numerik — menghitung rata-rata, median, dan standar deviasi cukup dengan satu baris kode. **pandas** membawa kemampuan ini lebih jauh dengan DataFrame yang mirip tabel spreadsheet, memungkinkan manipulasi data tabular seperti menambah kolom, memfilter baris, dan menampilkan data secara terstruktur.

Class `GradeBook` menggabungkan semua konsep dari tugas sebelumnya: menerima DataFrame sebagai atribut, menghitung statistik melalui method, dan menulis hasilnya ke file `.txt`. Ini menunjukkan bagaimana OOP menjadi "perekat" yang menyatukan data, logika, dan output dalam satu struktur yang rapi dan reusable.

### Refleksi Keseluruhan

Dari ketiga tugas ini, perkembangan konsepnya terlihat jelas: mulai dari **struktur data dasar** (tugas 4), ke **abstraksi melalui function dan class** (tugas 5), hingga **integrasi library dan file I/O** (tugas 6). Setiap tugas membangun di atas tugas sebelumnya — comprehension dari tugas 4 dipakai di tugas 6, function `rata_rata()` dari tugas 5 dipakai di class `Student`, dan OOP dari tugas 5 dikembangkan menjadi `GradeBook` di tugas 6.

Pemahaman ini relevan untuk bidang AI dan data science karena workflow-nya serupa: mengambil data, memprosesnya dengan NumPy/pandas, menganalisis hasilnya, lalu menyimpan output — semua terorganisir dalam class dan function yang modular.

---

## Cara Menjalankan (Tambahan sahaja)

```bash
# Pastikan Python 3.10+ terinstall
# Install dependency untuk tugas 6
pip install numpy pandas

# Jalankan masing-masing tugas
python tugas3.py
python tugas4.py
python tugas5.py
python tugas6.py
```

Tugas 6 akan menghasilkan file `ringkasan_tugas6.txt` di direktori yang sama.
