def fibo():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b  # Updating Values Simultaneously

fib = fibo()

for _ in range(20):  # Generating first 20 Fibonacci numbers
    print(next(fib))