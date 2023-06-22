"""
n = 4
* * * *
* * *
* *
*
"""
n=int(input("enter number"))
for i in range(n,0,-1):
   for ij in range(i):
      print("*",end=" ")
   print()
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()