# tugas4.py — Tugas 4: Python Data Structures
# Firman Fadilah — AI Development B10

# ============================================================
# 1. LIST — Akses & Manipulasi
# ============================================================

print("=" * 55)
print("  1. LIST — AKSES & MANIPULASI")
print("=" * 55)

data = ["Python", 42, "Bali", 3.14, True, "Kioku"]
print(f"  List awal : {data}")
print(f"  Elemen pertama  : {data[0]}")
print(f"  Elemen terakhir : {data[-1]}")

# Slicing [start:stop:step]
print(f"  Slicing [1:4]     : {data[1:4]}")
print(f"  Slicing [::2]     : {data[::2]}")
print(f"  Slicing [::-1]    : {data[::-1]}")

# Manipulasi
print(f"\n  Sebelum manipulasi : {data}")

data.append("AI")
print(f"  append('AI')       : {data}")

data.insert(2, "Udayana")
print(f"  insert(2,'Udayana'): {data}")

data.extend([100, 200])
print(f"  extend([100,200])  : {data}")

dihapus = data.pop(4)
print(f"  pop(4)             : {data}  (dihapus: {dihapus})")

data.remove(42)
print(f"  remove(42)         : {data}")


# ============================================================
# 2. TUPLE — Immutability & Unpacking
# ============================================================

print()
print("=" * 55)
print("  2. TUPLE — IMMUTABILITY & UNPACKING")
print("=" * 55)

mahasiswa = ("Firman", "Informatika", 2023, "Bali", 3.75)
print(f"  Tuple       : {mahasiswa}")
print(f"  Panjang     : {len(mahasiswa)}")
print(f"  Indeks [0]  : {mahasiswa[0]}")
print(f"  Indeks [2]  : {mahasiswa[2]}")
print(f"  Indeks [-1] : {mahasiswa[-1]}")

# Unpacking dengan *rest
nama, jurusan, *rest = mahasiswa
print(f"\n  Unpacking:")
print(f"  nama    = {nama}")
print(f"  jurusan = {jurusan}")
print(f"  *rest   = {rest}")

# Immutability demo
print(f"\n  Tuple bersifat immutable:")
print(f"  Mengubah elemen akan error — TypeError: 'tuple' does not support item assignment")


# ============================================================
# 3. SET — Keunikan & Operasi Himpunan
# ============================================================

print()
print("=" * 55)
print("  3. SET — KEUNIKAN & OPERASI HIMPUNAN")
print("=" * 55)

set_a = {"Python", "JavaScript", "TypeScript", "Java", "SQL"}
set_b = {"Python", "Java", "C++", "Rust", "Go"}

print(f"  Set A : {set_a}")
print(f"  Set B : {set_b}")

print(f"\n  Union (A | B)                : {set_a | set_b}")
print(f"  Intersection (A & B)         : {set_a & set_b}")
print(f"  Difference (A - B)           : {set_a - set_b}")
print(f"  Symmetric Difference (A ^ B) : {set_a ^ set_b}")

# Duplikat otomatis hilang
dengan_duplikat = [1, 2, 2, 3, 3, 3, 4, 4, 5]
tanpa_duplikat = set(dengan_duplikat)
print(f"\n  List dengan duplikat : {dengan_duplikat}")
print(f"  Setelah jadi set     : {tanpa_duplikat}")


# ============================================================
# 4. DICTIONARY — Key/Value Dasar
# ============================================================

print()
print("=" * 55)
print("  4. DICTIONARY — KEY/VALUE DASAR")
print("=" * 55)

mhs = {
    "nama": "Firman Fadilah",
    "nim": "2308561037",
    "angkatan": 2023,
    "kota": "Bali",
}
print(f"  Dict awal : {mhs}")

# Tambah key baru
mhs["jurusan"] = "Informatika"
print(f"  Tambah 'jurusan'  : {mhs}")

# Ubah nilai
mhs["kota"] = "Denpasar"
print(f"  Ubah 'kota'       : {mhs}")

# Hapus key
dihapus = mhs.pop("angkatan")
print(f"  Hapus 'angkatan'  : {mhs}  (dihapus: {dihapus})")

# keys, values, items
print(f"\n  keys()   : {list(mhs.keys())}")
print(f"  values() : {list(mhs.values())}")
print(f"  items()  : {list(mhs.items())}")

# Iterasi
print(f"\n  Iterasi key: value:")
for key, value in mhs.items():
    print(f"    {key}: {value}")


# ============================================================
# 5. NESTED STRUCTURES
# ============================================================

print()
print("=" * 55)
print("  5. NESTED STRUCTURES")
print("=" * 55)

buku = [
    {"judul": "Clean Code", "penulis": "Robert C. Martin", "tahun": 2008},
    {"judul": "The Pragmatic Programmer", "penulis": "David Thomas", "tahun": 2019},
    {"judul": "Designing Data-Intensive Applications", "penulis": "Martin Kleppmann", "tahun": 2017},
    {"judul": "Deep Learning", "penulis": "Ian Goodfellow", "tahun": 2016},
    {"judul": "Hands-On Machine Learning", "penulis": "Aurelien Geron", "tahun": 2022},
]

# Cetak semua judul
print("  Semua judul buku:")
for b in buku:
    print(f"    - {b['judul']} ({b['tahun']})")

# Filter buku terbit >= 2017 menggunakan list comprehension
buku_baru = [b for b in buku if b["tahun"] >= 2017]
print(f"\n  Buku terbit >= 2017:")
for b in buku_baru:
    print(f"    - {b['judul']} ({b['tahun']})")


# ============================================================
# 6. COMPREHENSION & UTILITAS
# ============================================================

print()
print("=" * 55)
print("  6. COMPREHENSION & UTILITAS")
print("=" * 55)

angka = list(range(1, 21))
print(f"  Angka 1-20 : {angka}")

# List comprehension — bilangan genap
genap = [x for x in angka if x % 2 == 0]
print(f"  Genap      : {genap}")

# List comprehension — kuadrat
kuadrat = [x ** 2 for x in angka]
print(f"  Kuadrat    : {kuadrat}")

# Dict comprehension — genap/ganjil mapping
mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print(f"\n  Dict genap/ganjil (1-10):")
for k, v in mapping.items():
    print(f"    {k}: {v}")

# Set comprehension — huruf unik dari kalimat
kalimat = "Belajar Python di Universitas Udayana"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print(f"\n  Kalimat     : '{kalimat}'")
print(f"  Huruf unik  : {sorted(huruf_unik)}")


# ============================================================
# 7. KEANGGOTAAN & PENCARIAN SEDERHANA
# ============================================================

print()
print("=" * 55)
print("  7. KEANGGOTAAN & PENCARIAN SEDERHANA")
print("=" * 55)

bahasa = ["Python", "JavaScript", "TypeScript", "SQL", "C++"]
bahasa_set = set(bahasa)

# Cek keanggotaan di list
cari = "Python"
print(f"  List   : {bahasa}")
print(f"  '{cari}' in list : {cari in bahasa}")

# Cek keanggotaan di set
cari2 = "Rust"
print(f"\n  Set    : {bahasa_set}")
print(f"  '{cari2}' in set  : {cari2 in bahasa_set}")

# Menggunakan index()
target = "TypeScript"
if target in bahasa:
    posisi = bahasa.index(target)
    print(f"\n  '{target}' ditemukan di list pada indeks {posisi}")
else:
    print(f"\n  '{target}' tidak ditemukan di list")

target2 = "Java"
if target2 in bahasa:
    posisi = bahasa.index(target2)
    print(f"  '{target2}' ditemukan di list pada indeks {posisi}")
else:
    print(f"  '{target2}' tidak ditemukan di list")


# ============================================================
print()
print("=" * 55)
print("  Selesai — Tugas 4 Python Data Structures")
print("=" * 55)
