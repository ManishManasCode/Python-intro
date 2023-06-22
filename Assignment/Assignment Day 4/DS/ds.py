class Pythonclass:

    def martix_mul(self,m,n):
        mul=[[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(m)):
            for j in  range(len(m[i])):
                for k in range(len(n[i])):
                   mul[i][j]+=m[i][k] * n[k][j]
        return mul
    
    def sum_array(self,n):
        sum=0
        for i in  range (len(n)):
            for j in range (len(n[i])):
                sum=sum+n[i][j]
        return sum
    
    def Two_D_array(self,n,m):
        for i in range(len(n)):
            for j in  range(len(n[0])):
                print(n[i][j] + m[i][j] , end=" ")
    
    def Diagonal(self,n):
        sum=0
        for i in range(len(n)):
            for j in  range(len(n[i])):
                if (i == j or i+j == len(n)-1):
                    sum=sum+n[i][j]
        return sum
    
    def Transpose(self,n):
        for i in range(len(n)):
            for j in range(len(n[0])):
                print(n[j][i], end=" ")
        print()