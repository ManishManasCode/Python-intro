def is_prime(x):
    for i in range(2, (x//2)+1):
        if x%i==0:
            return False 
    return True 

# def is_prime(x):
#     flag=0
#     i=1
#     while(i<=x):
#         if(x%i==0):
#             flag+=1
#         i+=1
#     if(flag==2):
#         return "it is a prime number"
#     else:
#         return "it is not a prime number"

# print(is_prime(9))
