#1.Program to calculate factorial of a number using iterative approach.

def factorial_iterative(n):
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer

# Input taken from the user
num = int(input("Enter a number: "))
print(f"Factorial of {num} : {factorial_iterative(num)}")

#2.Program to calculate factorial using recursive approach.

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


num = int(input("Enter a number: "))
print(f"Factorial of {num} (Recursive): {factorial_recursive(num)}")
