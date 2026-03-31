# tugas3.py — Tugas 3: Dasar Python
# Firman Fadilah — AI Development B10

# ============================================================
# 1. Deklarasi Variabel dan Tipe Data
# ============================================================

nama = "Firman Fadilah"           # string
semester = 6                       # integer
ipk = 3.75                         # float
sedang_magang = True               # boolean
bahasa = ["Python", "JavaScript", "TypeScript", "SQL", "Java"]  # list

print("=" * 55)
print("  1. DEKLARASI VARIABEL DAN TIPE DATA")
print("=" * 55)
print(f"  nama          = {nama} ({type(nama).__name__})")
print(f"  semester      = {semester} ({type(semester).__name__})")
print(f"  ipk           = {ipk} ({type(ipk).__name__})")
print(f"  sedang_magang = {sedang_magang} ({type(sedang_magang).__name__})")
print(f"  bahasa        = {bahasa} ({type(bahasa).__name__})")


# ============================================================
# 2. Manipulasi String
# ============================================================

print()
print("=" * 55)
print("  2. MANIPULASI STRING")
print("=" * 55)

salam = "Halo"
kampus = "Universitas Udayana"

# Menggabungkan string
gabungan = salam + ", saya " + nama + " dari " + kampus
print(f"  Gabungan   : {gabungan}")

# Panjang string
print(f"  Panjang nama '{nama}' : {len(nama)} karakter")

# Huruf besar dan kecil
print(f"  Uppercase  : {nama.upper()}")
print(f"  Lowercase  : {nama.lower()}")

# Replace
print(f"  Replace    : {kampus.replace('Udayana', 'UDAYANA')}")


# ============================================================
# 3. Operasi Matematika Sederhana
# ============================================================

print()
print("=" * 55)
print("  3. OPERASI MATEMATIKA")
print("=" * 55)

a = 25
b = 7

print(f"  a = {a}, b = {b}")
print(f"  a + b  = {a + b}")
print(f"  a - b  = {a - b}")
print(f"  a * b  = {a * b}")
print(f"  a / b  = {a / b:.2f}")
print(f"  a // b = {a // b}")
print(f"  a % b  = {a % b}")

# Contoh kalkulasi
total_sks = semester * 20
print(f"\n  Estimasi total SKS ({semester} semester x 20) = {total_sks} SKS")


# ============================================================
# 4. List dan Akses Elemen
# ============================================================

print()
print("=" * 55)
print("  4. LIST DAN AKSES ELEMEN")
print("=" * 55)

print(f"  List awal     : {bahasa}")
print(f"  Elemen ke-0   : {bahasa[0]}")
print(f"  Elemen ke-2   : {bahasa[2]}")
print(f"  Elemen terakhir : {bahasa[-1]}")

# Tambah item
bahasa.append("C++")
print(f"  Setelah append('C++') : {bahasa}")

# Hapus item
bahasa.remove("Java")
print(f"  Setelah remove('Java'): {bahasa}")

# Pop item terakhir
dihapus = bahasa.pop()
print(f"  Setelah pop()         : {bahasa} (dihapus: {dihapus})")

print(f"  Jumlah bahasa : {len(bahasa)} item")


# ============================================================
# 5. Input dari User
# ============================================================

print()
print("=" * 55)
print("  5. INPUT DARI USER")
print("=" * 55)

nama_user = input("  Masukkan nama kamu: ")
umur_user = input("  Masukkan umur kamu: ")

print()
print(f'  "Halo, nama saya {nama_user} dan umur saya {umur_user} tahun."')
print()
print("=" * 55)
print("  Terima kasih sudah menjalankan program ini!")
print("=" * 55)
