def Transpose(n):
    for i in range(len(n)):
        for j in range(len(n[0])):
            print(n[j][i], end=" ")
        print()

a=[[1,2,3],[4,5,6],[7,8,9]]
print(Transpose(a))