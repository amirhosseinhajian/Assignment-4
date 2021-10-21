n = int(input("Enter the n: "))
my_array = [0, 1]
if n <= 0:
    print("Please enter a positive number grater than 0")
elif n == 1:
    print(f"({my_array[0]})")
else:
    for i in range(2, n):
        my_array.append(my_array[i-1] + my_array[i-2])
    my_tuple = tuple(my_array)
    print(my_tuple)