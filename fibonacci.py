# fibonacci.py

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    print(fibonacci(n))