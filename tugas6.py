# tugas6.py — Tugas 6: Python Modules, File I/O, & OOP Sederhana
# Firman Fadilah — AI Development B10

import numpy as np
import pandas as pd

# Seed agar output konsisten
np.random.seed(42)


# ============================================================
# CLASS — GradeBook (OOP)
# ============================================================

class GradeBook:
    """Manajemen nilai mahasiswa menggunakan pandas DataFrame."""

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        """Rata-rata kolom nilai."""
        return round(self.df["nilai"].mean(), 2)

    def pass_rate(self, threshold: float = 70.0) -> float:
        """Persentase mahasiswa yang lulus (nilai >= threshold)."""
        lulus = (self.df["nilai"] >= threshold).sum()
        total = len(self.df)
        return round((lulus / total) * 100, 2) if total > 0 else 0.0

    def save_summary(self, path: str):
        """Menulis ringkasan ke file .txt."""
        jumlah_lulus = (self.df["status"] == "LULUS").sum()
        jumlah_tidak = (self.df["status"] == "TIDAK LULUS").sum()

        with open(path, "w", encoding="utf-8") as f:
            f.write("=" * 50 + "\n")
            f.write("  RINGKASAN TUGAS 6\n")
            f.write("  Firman Fadilah — AI Development B10\n")
            f.write("=" * 50 + "\n\n")

            f.write("--- Statistik NumPy (Nilai Ujian) ---\n")
            f.write(f"  Jumlah data    : {len(nilai_ujian)}\n")
            f.write(f"  Rata-rata      : {np.mean(nilai_ujian):.2f}\n")
            f.write(f"  Median         : {np.median(nilai_ujian):.2f}\n")
            f.write(f"  Standar Deviasi: {np.std(nilai_ujian):.2f}\n")
            f.write(f"  Nilai Min      : {np.min(nilai_ujian)}\n")
            f.write(f"  Nilai Max      : {np.max(nilai_ujian)}\n\n")

            f.write("--- Ringkasan DataFrame ---\n")
            f.write(f"  Jumlah baris      : {len(self.df)}\n")
            f.write(f"  Rata-rata nilai   : {self.average()}\n")
            f.write(f"  Jumlah LULUS      : {jumlah_lulus}\n")
            f.write(f"  Jumlah TIDAK LULUS: {jumlah_tidak}\n")
            f.write(f"  Persentase lulus  : {self.pass_rate()}%\n\n")

            f.write("--- Data Mahasiswa ---\n")
            f.write(self.df.to_string(index=False))
            f.write("\n\n" + "=" * 50 + "\n")

        print(f"  Ringkasan disimpan ke: {path}")

    def __str__(self) -> str:
        return (
            f"GradeBook(jumlah_data={len(self.df)}, "
            f"rata_rata={self.average()}, "
            f"lulus={self.pass_rate()}%)"
        )


# ============================================================
# DATA
# ============================================================

# Array NumPy — nilai ujian 15 mahasiswa
nilai_ujian = np.array([85, 72, 90, 65, 78, 55, 92, 88, 45, 76, 83, 60, 95, 70, 68])

# Data mahasiswa untuk DataFrame
data_mahasiswa = {
    "nama": [
        "Firman Fadilah", "Andi Pratama", "Siti Nurhaliza",
        "Budi Santoso", "Dewi Lestari", "Raka Wijaya",
        "Maya Putri", "Dimas Prasetyo"
    ],
    "nim": [
        "2308561037", "2308561012", "2308561023",
        "2308561045", "2308561056", "2308561067",
        "2308561078", "2308561089"
    ],
    "nilai": [85, 72, 90, 65, 78, 55, 92, 88],
}


# ============================================================
# DEMO
# ============================================================

if __name__ == "__main__":

    # ---- NUMPY ----
    print("=" * 55)
    print("  === NUMPY ===")
    print("=" * 55)

    print(f"  Data nilai ujian ({len(nilai_ujian)} data):")
    print(f"  {nilai_ujian}")
    print()
    print(f"  Rata-rata       : {np.mean(nilai_ujian):.2f}")
    print(f"  Median          : {np.median(nilai_ujian):.2f}")
    print(f"  Standar Deviasi : {np.std(nilai_ujian):.2f}")
    print(f"  Nilai Min       : {np.min(nilai_ujian)}")
    print(f"  Nilai Max       : {np.max(nilai_ujian)}")

    # ---- PANDAS ----
    print()
    print("=" * 55)
    print("  === PANDAS ===")
    print("=" * 55)

    df = pd.DataFrame(data_mahasiswa)

    # Tambah kolom status
    df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

    print("  DataFrame mahasiswa:")
    print()
    print(df.head(8).to_string(index=False))

    jumlah_lulus = (df["status"] == "LULUS").sum()
    jumlah_tidak = (df["status"] == "TIDAK LULUS").sum()
    print(f"\n  Jumlah LULUS      : {jumlah_lulus}")
    print(f"  Jumlah TIDAK LULUS: {jumlah_tidak}")

    # ---- FILE I/O ----
    print()
    print("=" * 55)
    print("  === FILE I/O ===")
    print("=" * 55)

    # ---- OOP: GRADEBOOK ----
    print()
    print("=" * 55)
    print("  === OOP: GRADEBOOK ===")
    print("=" * 55)

    gb = GradeBook(df)

    print(f"\n  {gb}")
    print(f"  Average    : {gb.average()}")
    print(f"  Pass Rate  : {gb.pass_rate()}%")
    print(f"  Pass Rate (threshold=80) : {gb.pass_rate(threshold=80.0)}%")

    # Simpan ringkasan ke file
    print()
    gb.save_summary("ringkasan_tugas6.txt")

    print()
    print("=" * 55)
    print("  Selesai — Tugas 6 Modules, File I/O, & OOP")
    print("=" * 55)
