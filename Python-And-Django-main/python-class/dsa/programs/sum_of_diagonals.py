a = [[1,2,3], 
     [4,5,6], 
     [7,8,9]]
s1=0
for i in range(len(a)):
    for j in range(len(a[i])):
            if (i == j or i+j == len(a)-1):
               s1=s1+a[i][j]
print(s1)      