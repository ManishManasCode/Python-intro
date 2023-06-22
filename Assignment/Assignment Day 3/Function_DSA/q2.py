def sum_array(n):
    sum=0
    for i in  range (len(n)):
        for j in range (len(n[i])):
            sum=sum+n[i][j]
    return sum


a=[[1,2,3],[4,5,6],[7,8,9]]
print(sum_array(a))