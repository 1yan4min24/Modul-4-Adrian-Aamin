def main():
    print("=== Program Login dan Input Mata Kuliah Mahasiswa ===")
    print("Catatan: Data autentikasi disimulasikan")

    # Langkah 1: Input Username
    username = input("Masukkan username: ")

    # Langkah 2: Input Password
    password = input("Masukkan password: ")

    # Langkah 3: Cek Login
    if cek_login(username, password):
        print("Login berhasil!")
        # Langkah 4: Input Mata Kuliah
        mata_kuliah = input_mata_kuliah()
        # Langkah 5: Daftar Dosen Pengampuh
        dosen_pengampuh = daftar_dosen()
        # Langkah 6: Pilih Dosen Pengampuh
        dosen_terpilih = pilih_dosen_pengampuh(dosen_pengampuh)
        # Langkah 7: Detail Data
        detail_data(username, mata_kuliah, dosen_terpilih)
    else:
        print("Login gagal. Username atau password salah.")

def input_mata_kuliah():
    return input("Masukkan nama mata kuliah: ")

def daftar_dosen():
    # Simulasi daftar dosen
    dosen_pengampuh = ["Dosen A", "Dosen B", "Dosen C"]
    return dosen_pengampuh

def pilih_dosen_pengampuh(dosen_pengampuh):
    print("Daftar dosen pengampuh:")
    for idx, dosen in enumerate(dosen_pengampuh, start=1):
        print(f"{idx}. {dosen}")

    while True:
        try:
            pilihan = int(input("Pilih dosen pengampuh (nomor): "))
            if 1 <= pilihan <= len(dosen_pengampuh):
                return dosen_pengampuh[pilihan - 1]
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan nomor yang valid.")

def detail_data(username, mata_kuliah, dosen_pengampuh):
    print("\nDetail Data:")
    print("Username:", username)
    print("Mata Kuliah:", mata_kuliah)
    print("Dosen Pengampuh:", dosen_pengampuh)

def cek_login(username, password):
    # Simulasi autentikasi
    data_mahasiswa = {
        "user1": "password1",
        "user2": "password2",
        "user3": "password3"
    }

    if username in data_mahasiswa:
        if data_mahasiswa[username] == password:
            return True
    return False

if __name__ == "__main__":
    main()
