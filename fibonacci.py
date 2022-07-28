#! python

def fibonacci(length):
    fibonacci_seq = [0, 1]
    while len(fibonacci_seq) < length:
        fibonacci_seq.append(sum(fibonacci_seq[-2:]))
    return fibonacci_seq


def recursive_fibonacci(length, fib_seq=(0, 1)):
    if len(fib_seq) == length:
        return fib_seq
    return recursive_fibonacci(length, fib_seq + (sum(fib_seq[-2:]),))


if __name__ == '__main__':
    length = 14
    fib_result = fibonacci(length)
    for fib_num in recursive_fibonacci(20):
        print(fib_num)
