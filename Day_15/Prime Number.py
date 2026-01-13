def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)
number = int(input())
if is_prime(number):
    print("Prime Number")
else:
    print("Not a Prime Number")
