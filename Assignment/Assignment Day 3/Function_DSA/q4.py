def Diagonal(n):
    sum=0
    for i in range(len(n)):
        for j in  range(len(n[i])):
            if (i == j or i+j == len(n)-1):
                sum=sum+n[i][j]
    return sum

a=[[1,2,3],[4,5,6],[7,8,9]]
print(Diagonal(a))    