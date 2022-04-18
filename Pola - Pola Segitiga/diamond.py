"""
      *
     ***
    *****
   *******
  *********
   *******
    *****
     ***
      *
"""

n = int(input("Masukan jumlah baris: "))

for row in range(n):
    print(" " * (n - row), "*" * (2 * row + 1))
for row in range(n - 2, -1, -1):
    print(" " * (n - row), "*" * (2 * row + 1))
