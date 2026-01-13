def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(input())
f=fibonacci(num-1)
print(f"The term {num} in the Fibonacci series is {f}")
