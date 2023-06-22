n = int(input())
temp= n
sum = 0
while n>0:
    rem = n%10
    sum = sum*10 + rem 
    n = n//10
# print(sum)
if temp == sum:
    print(True)
else:
    print(False)















# n = int(input("Enter a number: "))
# temp = n
# rev = 0

# while temp != 0:
#     rev  = rev * 10 + (temp % 10)
#     temp //= 10

# if rev == n:
#     print(f"{n} is a palindrome number")
# else:
#     print(f"{n} is not a palindrome number")