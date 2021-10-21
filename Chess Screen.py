n = int(input("Enter the n: "))
m = int(input("Enter the m: "))
for i in range(n):
    for j in range(m):
        if i % 2 == 0:
            if j % 2 == 0:
                print("#", end="")
            else:
                print("*", end="")
        else:
            if j % 2 == 0:
                print("*", end="")
            else:
                print("#", end="")
    print()