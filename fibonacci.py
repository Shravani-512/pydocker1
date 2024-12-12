# fibonacci.py
# fibonacci.py

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Set a predefined number of terms for the Fibonacci sequence
n = 10  # You can change this number to generate more or fewer Fibonacci numbers

# Generate and print the Fibonacci sequence
print(fibonacci(n))

