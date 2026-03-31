# tugas5.py — Tugas 5: Python Function and Class
# Firman Fadilah — AI Development B10


# ============================================================
# FUNCTIONS
# ============================================================

def greet(nama: str) -> str:
    """Mengembalikan teks sapaan."""
    return f"Halo, {nama}!"


def tambah(a: float, b: float = 0.0) -> float:
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b


def rata_rata(angka: list[float]) -> float:
    """Mengembalikan rata-rata list angka (2 desimal). Jika kosong, return 0.0."""
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


# ============================================================
# CLASS
# ============================================================

class Student:
    """Representasi data mahasiswa dengan nilai dan status kelulusan."""

    def __init__(self, nama: str, nim: str, nilai: list[float] | None = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float):
        """Menambah satu nilai ke list."""
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        """Menghitung rata-rata nilai menggunakan function rata_rata()."""
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        """LULUS jika rata-rata >= threshold, selain itu TIDAK LULUS."""
        return "LULUS" if self.rata_nilai() >= threshold else "TIDAK LULUS"

    def __str__(self) -> str:
        return (
            f"Student(nama='{self.nama}', nim='{self.nim}', "
            f"rata={self.rata_nilai()}, status={self.status()})"
        )


# ============================================================
# DEMO
# ============================================================

if __name__ == "__main__":

    print("=" * 55)
    print("  === FUNCTIONS ===")
    print("=" * 55)

    # greet
    print(f"  greet('Arifian')       : {greet('Arifian')}")
    print(f"  greet('Firman')        : {greet('Firman')}")

    # tambah
    print(f"\n  tambah(5, 7)           : {tambah(5, 7)}")
    print(f"  tambah(10)             : {tambah(10)}")
    print(f"  tambah(3.5, 2.5)       : {tambah(3.5, 2.5)}")

    # rata_rata
    print(f"\n  rata_rata([80, 90, 100])  : {rata_rata([80, 90, 100])}")
    print(f"  rata_rata([75, 60, 85])   : {rata_rata([75, 60, 85])}")
    print(f"  rata_rata([])             : {rata_rata([])}")

    print()
    print("=" * 55)
    print("  === CLASS STUDENT ===")
    print("=" * 55)

    # Mahasiswa 1 — nilai bagus
    mhs1 = Student("Firman Fadilah", "2308561037")
    mhs1.tambah_nilai(85)
    mhs1.tambah_nilai(92)
    mhs1.tambah_nilai(78)
    mhs1.tambah_nilai(90)

    print(f"\n  {mhs1}")
    print(f"  Daftar nilai : {mhs1.nilai}")
    print(f"  Rata-rata    : {mhs1.rata_nilai()}")
    print(f"  Status       : {mhs1.status()}")

    # Mahasiswa 2 — nilai kurang
    mhs2 = Student("Budi Santoso", "2308561099")
    mhs2.tambah_nilai(50)
    mhs2.tambah_nilai(65)
    mhs2.tambah_nilai(55)
    mhs2.tambah_nilai(60)

    print(f"\n  {mhs2}")
    print(f"  Daftar nilai : {mhs2.nilai}")
    print(f"  Rata-rata    : {mhs2.rata_nilai()}")
    print(f"  Status       : {mhs2.status()}")

    # Custom threshold
    print(f"\n  Status mhs2 (threshold=50) : {mhs2.status(threshold=50.0)}")

    print()
    print("=" * 55)
    print("  Selesai — Tugas 5 Python Function and Class")
    print("=" * 55)
