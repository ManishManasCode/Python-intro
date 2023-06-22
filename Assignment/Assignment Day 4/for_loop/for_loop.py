class Python_Class:

    # Factorial
    def factorial(self,n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
            print(f"{n}! = {fact}")
        print(fact)
    #fibnoci
    def fibnoci(self,n):
        a=0
        b=1
        for i in  range(1,n+1):
            c=a+b
            a=b
            b=c
            print(f"{i}th fibonacci number = {c}")
    #prime number
    def prime(self,n):
        isPrime = True 
        for i in range(2,int(n/2)):
            if n % i == 0:
                isPrime = False 
                break 

        if isPrime:
            print(f"{n}, is  a Prime Number") 
        else:
            print(f"{n}, is not  a Prime Number")
    
    #prime factors
    def primefactors(self,n):
        i=0
        for i in range(1,n+1):
            if n%i==0:
                print(f"{i} is a factor")
    #Table

    def table(self,n,t):
        for i in range(1,t+1):
            print(f"{n} X {t} = {n*i}")