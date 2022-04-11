rows = int(input("Masukan Jumlah Baris: "))

for row in range(rows):
    for column in range(row + 1):
        print("*", end="")
    print()
