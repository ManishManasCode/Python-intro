n=int(input())
for i in range(n,0,-1):
    #print (i,end="")
    for j in range(1,i):
        print(" ", end=" ")
    for k in range(n-i+1):
        print("*", end=" ")
    print()
