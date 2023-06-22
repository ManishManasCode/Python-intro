def Two_D_array(n,m):
    for i in range(len(n)):
        for j in  range(len(n[0])):
            print(n[i][j] + m[i][j] , end=" ")
    

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]

print(Two_D_array(a,b))