n = int(input())
isPrime = True 
for i in range(2,int(n/2)):
    if n % i == 0:
        isPrime = False 
        break 

if isPrime:
    print(f"{n}, is  a Prime Number") 
else:
    print(f"{n}, is not  a Prime Number") 


# n=int(input())
# i=1
# flag=0
# for i in range(1,n+1):
#     if(n%i==0):
#         flag+=1
#     i+=1
# if(flag==2):
#     print(f"the {n} is prime number")
# else:
#     print(f"the {n} is not prime number")
    

    

