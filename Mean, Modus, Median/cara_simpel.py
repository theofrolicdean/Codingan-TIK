jumlah_bilangan = int(input("Masukan jumlah bilangan: "))
bilangan = []

for index in range(jumlah_bilangan):
    input_user = int(input(f"Masukan Bilangan Ke-{index + 1}: "))
    bilangan.append(input_user)

# Mean
mean = sum(bilangan) / len(bilangan)

# Modus
modus = max(bilangan, key=bilangan.count)

# Median
index = jumlah_bilangan // 2
median = None

if jumlah_bilangan % 2:
    median = sorted(bilangan)[index]
else:
    median = sum(sorted(bilangan)[index - 1:index + 1]) / 2

# Print Mean, Modus, Media
print(f"Mean: {mean}")
print(f"Modus: {modus}")
print(f"Median: {median}")
