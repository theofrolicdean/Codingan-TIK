"""
    *
   ***
  *****
 *******
*********
"""

n = int(input("Enter number of rows: "))
column = 0

for row in range(1, n + 1):
    for space in range(1, (n - row) + 1):
        print(end=" ")
    while column != (2 * row - 1):
        print("*", end="")
        column += 1
    column = 0
    print()
