"""
    *
    **
    ***
    ****
    *****
"""
n = int(input("Masukan jumlah baris: "))

for row in range(n):
    for column in range(row + 1):
        print("*", end="")
    print()
