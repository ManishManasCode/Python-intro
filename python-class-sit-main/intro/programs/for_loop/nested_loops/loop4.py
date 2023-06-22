"""
n = 5
    *
   * *
  * * *
 * * * *
* * * * *
"""
n = int(input("Enter no. of terms: "))
l = n-1
for i in range(n):
    for j in range(l):
        print(end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()
    l-=1
