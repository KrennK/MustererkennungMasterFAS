# Modul Fibonacci Zahlen
def fib(n):    # gebe die Fibonacci Zahlen bis n aus
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
