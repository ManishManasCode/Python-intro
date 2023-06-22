def palidrome(n):
    temp=n
    sum = 0
    while n > 0:
        rem = n%10
        sum = sum*10 + rem
        n= n//10

    if temp == sum:
        print(True)
    else:
        print(False)

n=int(input())
palidrome(n)