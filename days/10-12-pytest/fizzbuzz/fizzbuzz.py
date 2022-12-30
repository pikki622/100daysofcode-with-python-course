def fizzbuzz(n):
    if n % 3 == 0:
        return 'Fizz Buzz' if n % 5 == 0 else 'Fizz'
    return 'Buzz' if n % 5 == 0 else n
