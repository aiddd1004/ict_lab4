n = int(input("Enter number of terms: "))

if n <= 0:
    print("Enter a positive number")
else:
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b
