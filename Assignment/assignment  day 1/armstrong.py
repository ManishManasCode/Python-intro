n=int(input())

size=0
num1 = n
num2 = n

while num1 > 0:
    num1=int(num1/10)
    size +=1
print(size)
sum=0
while num2 > 0:
    rem=num2 % 10
    num2 = int(num2/10)
    sum += (rem**size)

if sum == n:
    print(f"{n} is a Armstrong number")
else:
    print(f"{n} is not a ArmStrong number")


