print("PROGRAM PYTHON MENENTUKAN NILAI SISWA")

run = True
while run:

    nilai_praktek = float(input("\nMasukan Nilai Praktek: "))
    nilai_uts = float(input("Masukan Nilai UTS: "))
    nilai_uas = float(input("Masukan Nilai UAS: "))
    nilai_akhir = (0.15 * nilai_praktek) + \
        (0.35 * nilai_uts) + (0.5 * nilai_uas)

    if nilai_akhir >= 80:
        indeks = "A"
    elif nilai_akhir >= 70:
        indeks = "B"
    elif nilai_akhir >= 55:
        indeks = "C"
    elif nilai_akhir >= 40:
        indeks = "D"
    else:
        indeks = "E"

    print(f"Nilai Akhir: {nilai_akhir}")
    print(f"Nilai Indeks: {indeks}")

    ulang = input("Ulangi Program (y/n): ")
    if ulang.lower() == 'y':
        continue
    if ulang.lower() == 'n':
        run = False

print("Goodbye! :D")