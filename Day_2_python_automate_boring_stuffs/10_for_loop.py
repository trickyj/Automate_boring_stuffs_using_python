# 10 example of forloop to get this clear.
# 1: loop through a range of numbers and print each numbers:

for i in range(1, 6):
    print(i)

# 2: Iterate over a list and print each item:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# 3: Calcuate the sum of numbers in a list:

numbers = [1, 2, 3, 4, 5, 6]
sum = 0
for number in numbers:
    sum += number
print("sum: ", sum)


# 4: iterate over a string and print each character:

text = "hello, python!"
for char in text:
    print(char)

# 5: Loop through a dictionary and print key-value pairs:

person = {"name": "john", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)

# 6 Loop through a list of tuples and print elements:

coordinates = [(1, 2), (3, 5), (4, 6), (9, 1)]
for x, y in coordinates:
    print("X: ", x, "Y: ", y)


# 7 Print even numbers in a range:

for num in range(1, 11):
    if number % 2 == 0:
        print(num)

# 8: Iterate through a list and find the length of each item:

languages = ["Python", "Java", "C++", "JavaScript"]
for lang in languages:
    print(lang, "has", len(lang), "characters")

# 9: loop through a list and check for specific values:

scores = [85, 92, 23, 95, 88]
for score in scores:
    if score >= 90:
        print("High Score: ", score)

# 10: nested for loops to create a multiplication table:

for i in range(1, 6):
    for j in range(1, 6):
        product = i * j
        print(i, "x", j, "=", product)
