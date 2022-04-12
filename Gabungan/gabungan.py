NAMA = input("Masukan Nama: ")
KELAS = input("Masukan Kelas: ")

while True:
    try:
        NO_ABSEN = int(input("No. Absen: "))
        if NO_ABSEN < 0:
            print("No. Absen tidak bisa negatif")
        else:
            break
    except ValueError:
        print("No. Absen yang dimasukan tidak valid.")

TOTAL = None
BILANGAN = []

while True:
    try:
        TOTAL = int(input("Masukan Jumlah Bilangan: "))
        if TOTAL < 0:
            print("Nilai jumlah bilangan tidak bisa negatif")
        else:
            break
    except ValueError:
        print("Nilai jumlah bilangan yang dimasukan tidak valid.")

for index in range(TOTAL):
    user_input = int(input(f"Masukan Bilangan Ke-{index + 1}: "))
    BILANGAN.append(user_input)

mean = sum(BILANGAN) / len(BILANGAN)

modus = max(BILANGAN, key=BILANGAN.count)
index = TOTAL // 2
median = None

if TOTAL % 2:
    median = sorted(BILANGAN)[index]
else:
    median = sum(sorted(BILANGAN)[index - 1:index + 1]) / 2

print(f"Mean: {mean}")
print(f"Modus: {modus}")
print(f"Median: {median}")

VOLUME = BILANGAN[0] * BILANGAN[1] * BILANGAN[2]
print(f"Volume: {VOLUME}")

SYMBOL = input("Masukan simbol: ")
for row in range(TOTAL):
    for column in range(row + 1):
        print(SYMBOL, end="")
    print()
