#for loop using prime number
#n=int(input())
#flag=0
#for i in range(2,n):
#    if n%i==0:
#        flag+=1
#    i=i+1
#    if flag==0:
#        print(n,"is a prime number")
#        break
#    else:
#        print(n,"is  not a prime number")
#        break
#while loop using prime number
n=int(input())
flag=0
while n>=1:
    if n%1==0:
        flag+=1
        n=n-1
    else:
        print(n,"is  not a prime number")
        break
    if flag==0:
        print(n,"is a prime number")
    
