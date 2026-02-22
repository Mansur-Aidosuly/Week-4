# Example 1 – Simple counter
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

for num in Counter(3):
    print(num)

# Example 2 – Even numbers
class EvenNumbers:
    def __init__(self, max_num):
        self.max = max_num
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 2
        if self.num <= self.max:
            return self.num
        raise StopIteration

for n in EvenNumbers(10):
    print(n)

# Example 3 – Reverse iterator
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

for item in Reverse([1, 2, 3]):
    print(item)

# Example 4 – Infinite iterator (manual break)
class Infinite:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return self.num

it = Infinite()
for _ in range(5):
    print(next(it))

# Example 5 – Fibonacci iterator
class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.limit:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value

for f in Fibonacci(10):
    print(f)