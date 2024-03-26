def hitung_diskon(total_belanja):
    if total_belanja >= 250000:
        diskon = total_belanja * 50 / 100
        return diskon
    else:
        return None

def input_total_belanja():
    while True:
        try:
            total_belanja = float(input("Masukkan total belanja (Rp): "))
            if total_belanja < 0:
                print("Total belanja tidak boleh negatif.")
                continue
            return total_belanja
        except ValueError:
            print("Masukkan angka yang valid.")

def main():
    print("Selamat datang di Program Hitung Diskon!")

    total_belanja = input_total_belanja()

    diskon = hitung_diskon(total_belanja)

    if diskon is not None:
        total_bayar = total_belanja - diskon
        print("Total belanja Anda sebesar Rp.", total_belanja)
        print("Anda mendapatkan diskon sebesar Rp.", diskon)
        print("Total yang harus Anda bayar adalah Rp.", total_bayar)
    else:
        print("Total belanjaan Anda sebesar Rp.", total_belanja)
        print("Maaf, Anda tidak mendapatkan diskon karena total belanjaan tidak mencapai Rp. 250.000.")
        print("Total yang harus Anda bayar adalah Rp.", total_belanja)

if __name__ == "__main__":
    main()
