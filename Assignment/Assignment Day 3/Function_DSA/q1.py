def martix_mul(m,n):
    mul=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(m)):
        for j in  range(len(m[i])):
            for k in range(len(n[i])):
               mul[i][j]+=m[i][k] * n[k][j]
    return mul

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[1,2,3],[4,5,6],[7,8,9]]

print(martix_mul(a,b))