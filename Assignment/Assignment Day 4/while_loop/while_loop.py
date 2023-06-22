class Pythonclass:

    def palindrome(self,n):
        temp= n
        sum = 0
        while n>0:
            rem = n%10
            sum = sum*10 + rem 
            n = n//10
        if temp == sum:
            print(True)
        else:
            print(False)

    def table(self,n,t):
        i=1
        while i<=t:
            print(n,"*",i,"=",n*i)
            i=i+1

    def size_number(self,n):
        c=0
        while n!=0:
            n=n//10
            c=c+1
        
    def primefactor(self,n):
        i=1
        while(i<=n):
            if n%i==0:
                print(f"{i} is a prime factor")
                i=i+1
    
    def prime_number(self,n):
        i=1
        flag=0
        while(i<=n):
            if(n%i==0):
                flag+=1
                i+=1
        if(flag==2):
            print(f"the {n} is prime number")
        else:
            print(f"the {n} is not prime number")
    
