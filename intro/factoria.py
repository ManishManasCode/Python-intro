#n=int(input())
#i=0
#for i in range(1,n+1):
#    if n%i==0:
#        print(f"{i} is a factor")


#while in factor
n=int(input())
i=1
while i<=n:
    if n%i==0:
        print(f"{i} is a factor")
        i=i+1