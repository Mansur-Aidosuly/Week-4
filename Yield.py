# Example 1 – Simple generator
def gen_numbers():
    yield 1
    yield 2
    yield 3

for n in gen_numbers():
    print(n)

# Example 2 – Squares
def squares(n):
    for i in range(n):
        yield i * i

for s in squares(5):
    print(s)

# Example 3 – Even numbers
def evens(limit):
    for i in range(0, limit, 2):
        yield i

for e in evens(10):
    print(e)

# Example 4 – String characters
def chars(text):
    for ch in text:
        yield ch

for c in chars("Hi"):
    print(c)

# Example 5 – Countdown
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x)