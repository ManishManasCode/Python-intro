a = [[1,2,3], 
     [4,5,6], 
     [7,8,9]]

b = [[1,2,3], 
     [4,5,6], 
     [7,8,9]]

c = []
x = len(a)
y = len(a[0])

for i in range(x):
    for j in range(y):
        print(a[i][j] + b[i][j], end = " ")
    print()
