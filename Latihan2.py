def hitung_nilai_akhir(kehadiran, nilai_tugas, nilai_uts, nilai_uas):
    # Hitung total nilai kehadiran (16x)
    total_kehadiran = kehadiran * 16
    
    # Hitung rata-rata nilai tugas
    rata_tugas = sum(nilai_tugas) / len(nilai_tugas)
    
    # Hitung nilai akhir berdasarkan bobot
    nilai_akhir = (total_kehadiran * 0.2) + (rata_tugas * 0.2) + (nilai_uts * 0.3) + (nilai_uas * 0.3)
    
    return nilai_akhir

def tentukan_hasil_nilai(nilai_akhir):
    if nilai_akhir >= 90:
        return "A"
    elif nilai_akhir >= 80:
        return "B"
    elif nilai_akhir >= 70:
        return "C"
    elif nilai_akhir >= 60:
        return "D"
    else:
        return "E"

def main():
    print("=== Program Menghitung Nilai Akhir Mahasiswa ===")
    print("Catatan: Silakan masukkan nilai dalam skala 0-100")

    # Input nilai kehadiran
    while True:
        try:
            kehadiran = int(input("Masukkan jumlah kehadiran mahasiswa: "))
            if kehadiran < 0:
                print("Jumlah kehadiran tidak boleh negatif.")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid.")

    # Input nilai tugas
    nilai_tugas = []
    for i in range(1, 9):
        while True:
            try:
                nilai = float(input(f"Masukkan nilai tugas {i}: "))
                if not 0 <= nilai <= 100:
                    print("Nilai tugas harus dalam skala 0-100.")
                    continue
                nilai_tugas.append(nilai)
                break
            except ValueError:
                print("Masukkan angka yang valid.")

    # Input nilai UTS
    while True:
        try:
            nilai_uts = float(input("Masukkan nilai UTS: "))
            if not 0 <= nilai_uts <= 100:
                print("Nilai UTS harus dalam skala 0-100.")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid.")

    # Input nilai UAS
    while True:
        try:
            nilai_uas = float(input("Masukkan nilai UAS: "))
            if not 0 <= nilai_uas <= 100:
                print("Nilai UAS harus dalam skala 0-100.")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid.")

    # Hitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(kehadiran, nilai_tugas, nilai_uts, nilai_uas)

    # Tentukan hasil nilai
    hasil_nilai = tentukan_hasil_nilai(nilai_akhir)

    # Tampilkan hasil
    print("\n=== Hasil Perhitungan ===")
    print("Nilai akhir mahasiswa adalah:", nilai_akhir)
    print("Hasil nilai akhir mahasiswa adalah:", hasil_nilai)

if __name__ == "__main__":
    main()
