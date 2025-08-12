def fib_seq(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_seq(n) + fib_seq(n-1)