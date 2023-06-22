n=int(input())
l=n-1
for i in range(n):
    for j in range(n):
        print(end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()
    l-=1