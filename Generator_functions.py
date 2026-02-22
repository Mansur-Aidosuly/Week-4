# Example 1
def numbers():
    for i in range(3):
        yield i

print(list(numbers()))

# Example 2
def multiply_by_two(n):
    for i in range(n):
        yield i * 2

print(list(multiply_by_two(5)))

# Example 3
def powers_of_two(n):
    for i in range(n):
        yield 2 ** i

print(list(powers_of_two(5)))

# Example 4
def filter_positive(nums):
    for num in nums:
        if num > 0:
            yield num

print(list(filter_positive([-2, 3, -1, 5])))

# Example 5
def words(sentence):
    for word in sentence.split():
        yield word

print(list(words("Hello world Python")))