def hitung_molaritas(mol, volume_liter):
    return mol / volume_liter

def hitung_normalitas(eq, volume_liter):
    return eq / volume_liter

def main():
    print("KALKULATOR KIMIA: Molaritas dan Normalitas\n")

    print("1. Hitung Molaritas (mol/L)")
    print("2. Hitung Normalitas (eq/L)")
    pilihan = input("Pilih perhitungan (1/2): ")

    if pilihan == "1":
        mol = float(input("Masukkan jumlah mol zat (mol): "))
        volume = float(input("Masukkan volume larutan (liter): "))
        molaritas = hitung_molaritas(mol, volume)
        print(f"Molaritas = {molaritas:.2f} mol/L")

    elif pilihan == "2":
        eq = float(input("Masukkan jumlah ekivalen zat (eq): "))
        volume = float(input("Masukkan volume larutan (liter): "))
        normalitas = hitung_normalitas(eq, volume)
        print(f"Normalitas = {normalitas:.2f} eq/L")

    else:
        print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")

if __name__ == "__main__":
    main()
