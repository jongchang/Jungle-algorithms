def factorial(n):
    if (n == 1) or ( n == 0):
        return 1

    result = n * factorial(n-1)
    return result

N = int(input())

print(factorial(N))