"""
n = 5

*       *
  *   *
    *
  *   *
*       *
    


"""
n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        # print(f"{i},{j}", end=" ")
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()