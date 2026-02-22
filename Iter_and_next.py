# Example 1 – List
numbers = [10, 20, 30]
it1 = iter(numbers)
print(next(it1))
print(next(it1))
print(next(it1))

# Example 2 – String
text = "ABC"
it2 = iter(text)
print(next(it2))
print(next(it2))

# Example 3 – Tuple
t = (1, 2, 3)
it3 = iter(t)
print(next(it3))

# Example 4 – Set
s = {5, 6, 7}
it4 = iter(s)
print(next(it4))

# Example 5 – StopIteration example
nums = [1]
it5 = iter(nums)
print(next(it5))
# print(next(it5))  # Uncommenting this will raise StopIteration