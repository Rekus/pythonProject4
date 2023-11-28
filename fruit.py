fruit = ["apple", "banana", "orange", "kiwi", "pear"]

fruit.sort()
print(fruit)

for fruit in sorted(fruit):
    if fruit.startswith("a"):
        print(fruit)