"""
n = 5
* * * * *
 * * * *
  * * *
   * *
    *
"""
n=int(input())
l=n-1

for i in range (n):
    for j in range (n-l):
        print("",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    l-=1
    print()