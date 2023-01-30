# A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Endless Fibonacci
def fib_endless_gen():
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while True:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    for i, f in enumerate(fib_endless_gen()):
        if i == 100:
            break
        print(f)