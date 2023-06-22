class Pyhton_Class:
    
    #Even And Odd
    def even_odd(self,n):
        if n%2==0:
            print(f"{n} is an even number")
        else:
            print(f"{n} is an odd number")
        
    #Leap year or not
    def leapyear(self,n):
        if n % 100 == 0:
            if n % 400 == 0:
                print(f"{n} is a leap year")
            else:
                print(f"{n} is not a leap year")
        else:
            if n % 4 == 0:
                print(f"{n} is a leap year")
            else:
                print(f"{n} is not a leap year")
        
    

    