a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(a)):
    for j in  range(len(a[0])):
        print(a[i][j] + b[i][j] , end=" ")
    print()