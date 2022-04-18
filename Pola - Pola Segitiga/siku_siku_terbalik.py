"""
    *****
    ****
    ***
    **
    *
"""

n = int(input("Masukan jumlah baris: "))

for row in range(n, 0, -1):
    n += 1
    for j in range(row):
        print("*", end="")
    print()
