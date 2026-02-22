import random

# Example 1 – random() (float between 0 and 1)
print("Random float:", random.random())

# Example 2 – randint(a, b)
print("Random integer 1 to 10:", random.randint(1, 10))

# Example 3 – choice()
fruits = ["apple", "banana", "cherry"]
print("Random fruit:", random.choice(fruits))

# Example 4 – shuffle()
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("Shuffled cards:", cards)

# Example 5 – random in range with step
print("Random even number from 0 to 10:",
      random.choice(range(0, 11, 2)))