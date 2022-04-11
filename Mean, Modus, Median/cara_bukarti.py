N = int(input("Masukan jumlah bilangan: "))
array_data = [0 for _ in range(N)]
for i in range(N):
    print(f"Masukan Bilangan Ke-{i + 1}: ", end="")
    array_data[i] = int(input())

array_count = [0 for _ in range(100)]
sum = 0.0

for i in range(N):
    x = array_data[i]
    sum += x
    array_count[x] += 1

mean = sum / N
modus_count = 0
modus = 0
for i in range(100):
    x = array_count[i]
    if (x > modus):
        modus_count = x
        modus = i

for i in range(N):
    idxmin = i
    for j in range(i + 1, N):
        if array_data[j] < array_data[idxmin]:
            idxmin = j
    array_data[i], array_data[idxmin] = array_data[idxmin], array_data[i]

if N % 2 == 0:
    median = (array_data[N // 2] + array_data[N // 2 - 1]) / 2
else:
    median = array_data[N // 2]

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Modus: {modus}")
