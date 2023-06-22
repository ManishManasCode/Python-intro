a=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in range(len(a)):
    for j in range(len(a[i])):
        if (i == j or i+j == len(a)-1):
            sum=sum+a[i][j]
print(sum)