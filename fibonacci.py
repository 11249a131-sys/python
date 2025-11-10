def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Sequence:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
try:
    N = int(input("Enter the number of terms (N > 0): "))
    if N <= 0:
        print("Error: Invalid input! Please enter a number greater than 0.")
    else:
        fibonacci(N)
except ValueError:
    print("Error: Please enter a valid integer.")

