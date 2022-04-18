"""
*******
 *****
  ***
   *
"""

n = int(input("Enter number of rows: "))

for row in range(n, 1, -1):
    for space in range(n - row):
        print(" ", end="")
    for column in range(row, 2 * row - 1):
        print("*", end="")
    for column in range(1, row - 1):
        print("*", end="")
    print()
