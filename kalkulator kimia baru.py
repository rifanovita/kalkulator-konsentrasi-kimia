import tkinter as tk
from tkinter import messagebox

def ambil_nilai(entry, nama_field):
    try:
        return float(entry.get())
    except ValueError:
        raise ValueError(f"{nama_field} tidak valid!")

def hitung_molaritas():
    try:
        mol = ambil_nilai(entry_mol, "Mol")
        volume = ambil_nilai(entry_volume, "Volume")
        hasil = mol / volume
        messagebox.showinfo("Hasil", f"Molaritas = {hasil:.4f} M")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hitung_normalitas():
    try:
        mol = ambil_nilai(entry_mol, "Mol")
        volume = ambil_nilai(entry_volume, "Volume")
        valensi = int(entry_valensi.get())
        hasil = (mol * valensi) / volume
        messagebox.showinfo("Hasil", f"Normalitas = {hasil:.4f} N")
    except ValueError:
        messagebox.showerror("Error", "Input tidak valid!")

def hitung_molalitas():
    try:
        mol = ambil_nilai(entry_mol, "Mol")
        massa = ambil_nilai(entry_massa_pelarut, "Massa Pelarut")
        hasil = mol / massa
        messagebox.showinfo("Hasil", f"Molalitas = {hasil:.4f} m")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def hitung_ppm():
    try:
        massa = ambil_nilai(entry_massa_zat, "Massa Zat")
        volume = ambil_nilai(entry_volume, "Volume")
        hasil = (massa / volume) * 1_000_000
        messagebox.showinfo("Hasil", f"PPM = {hasil:.2f} ppm")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Kalkulator Konsentrasi Kimia")

# Komponen input
field_data = [
    ("Jumlah Mol (mol):", "entry_mol"),
    ("Volume Larutan (L):", "entry_volume"),
    ("Massa Pelarut (kg):", "entry_massa_pelarut"),
    ("Valensi:", "entry_valensi"),
    ("Massa Zat (mg):", "entry_massa_zat"),
]

entries = {}
for i, (label_text, var_name) in enumerate(field_data):
    tk.Label(root, text=label_text).grid(row=i, column=0)
    entries[var_name] = tk.Entry(root)
    entries[var_name].grid(row=i, column=1)

entry_mol = entries["entry_mol"]
entry_volume = entries["entry_volume"]
entry_massa_pelarut = entries["entry_massa_pelarut"]
entry_valensi = entries["entry_valensi"]
entry_massa_zat = entries["entry_massa_zat"]

# Tombol perhitungan
tk.Button(root, text="Hitung Molaritas", command=hitung_molaritas).grid(row=5, column=0, pady=5)
tk.Button(root, text="Hitung Normalitas", command=hitung_normalitas).grid(row=5, column=1, pady=5)
tk.Button(root, text="Hitung Molalitas", command=hitung_molalitas).grid(row=6, column=0, pady=5)
tk.Button(root, text="Hitung PPM", command=hitung_ppm).grid(row=6, column=1, pady=5)

root.mainloop()
