"""_summary_

    Raises:
        StopIteration: _description_

    Returns:
        _type_: _description_

    Yields:
        _type_: _description_

"""


class PrimeIterator:
    def __init__(self, max):
        self.max = max
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        while not self.is_prime(self.number):
            self.number += 1
        if self.number >= self.max:
            raise StopIteration
        return self.number

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


# Example usage
for prime in PrimeIterator(25):
    print(prime)


def multiples_of_five(n):
    for i in range(n):
        yield i * 5


# Example usage
result = list(multiples_of_five(10))
print(result)


def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func


closure = outer_func(10)
print(closure(5))  # Output: 15


