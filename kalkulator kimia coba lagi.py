print("Kalkulator Kimia Sederhana")
print("1 = Molaritas")
print("2 = Normalitas")

p = input("Pilih (1/2): ")
a = float(input("Masukkan mol atau ekivalen: "))
b = float(input("Masukkan volume (liter): "))

hasil = a / b

if p == "1":
    print("Molaritas =", hasil, "mol/L")
elif p == "2":
    print("Normalitas =", hasil, "eq/L")
else:
    print("Pilihan salah.")
