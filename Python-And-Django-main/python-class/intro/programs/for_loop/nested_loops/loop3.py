"""
n = 4
      *
    * *
  * * *
* * * *
"""
"""
o o o -> 3
o o   -> 2
o     -> 1
"""

n = int(input())
for i in range(n,0, -1):
  # print(i, end=" ")
  for j in range(1,i):
    print(" ", end=" ")
  for k in range(n-i+1):
    print("*", end=" ")
  print()














# pattern_range = int(input("Enter the range: "))
# for i in range(1,pattern_range + 1):
#     for j in range(i,pattern_range):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()