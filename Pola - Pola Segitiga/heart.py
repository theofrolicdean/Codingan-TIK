"""
    *         * 
   * *       * *
  * * *     * * *
 * * * *   * * * *
* * * * * * * * * *
* * * * * * * * * *
 * * * * * * * * *
  * * * * * * * *
   * * * * * * *
    * * * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
"""

n = int(input("Masukan jumlah baris: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    for j in range(2 * (n - i - 1)):
        print(" ", end="")
    for j in range(i + 1):
        print("* ", end="")
    print()
for i in range(2 * n, 0, -1):
    for j in range(2 * n - i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()
