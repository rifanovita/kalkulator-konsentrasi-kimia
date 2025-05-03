print("KALKULATOR KIMIA SEDERHANA")
print("1. Molaritas (mol/L)")
print("2. Normalitas (eq/L)")

pilih = input("Pilih 1 atau 2: ")

if pilih == "1":
    mol = float(input("Masukkan mol zat: "))
    volume = float(input("Masukkan volume (liter): "))
    M = mol / volume
    print("Molaritas =", M, "mol/L")

elif pilih == "2":
    eq = float(input("Masukkan ekivalen zat: "))
    volume = float(input("Masukkan volume (liter): "))
    N = eq / volume
    print("Normalitas =", N, "eq/L")

else:
    print("Pilihan tidak valid.")
