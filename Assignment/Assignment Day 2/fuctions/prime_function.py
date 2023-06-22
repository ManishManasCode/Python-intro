def isprime(n):
    flag=True
    for i in range(2,int(n/2)):
        if n % i ==0:
            flag = False
            break
    if flag:
        print(f"{n}, is  a Prime Number") 
    else:
        print(f"{n}, is not  a Prime Number") 
    
n=int(input())
isprime(n)
