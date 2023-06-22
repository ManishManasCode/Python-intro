n_loop = int(input())
for i in range(1,n_loop):
    n = i 
    size = 0
    num1 = n 
    num2 = n
    while num1 > 0:
        num1 = int(num1/10)
        size +=1 
    # print(size)
    sum = 0
    while num2 > 0:
        rem = num2 % 10 
        num2 = int(num2/10)
        sum += (rem**size)
    # print(sum, i)
    if sum == i:
        print(f"{i} is a Armstrong number")
    # else:
    #     print(f"{n} is not an armstrong number") 


# n=int(input("Enter a number"))
# c=0
# num=0
# while n!=0:
#     n=n//10
#     c+=1
# #print(c)
# while n:
#     n=n//10
#     num=n**c
#     num+=num
# print(num)