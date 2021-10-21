n = int(input("Enter the n: "))
m = int(input("Enter the m: "))
for i in range(1, n+1):
    for j in range(1, m+1):
        print(i*j , end="\t")
    print()