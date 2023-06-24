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