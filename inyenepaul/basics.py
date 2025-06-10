name = "Inyene Paul"
favorite_food = "beans and rice"

print("Hello, my name is", name)
print("My favorite food is", favorite_food)
print("Python Bootcamp")

a = 7
b = 3
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a // b)  # Floor division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation

a = 42
check for data type
if isinstance(a, int):
    print("a is an integer")

a = 3.14
if isinstance(a, float):
    print("a is a float")

a = "Hello"
if isinstance(a, str):
    print("a is a string")

a = [1, 2, 3]
if isinstance(a, list):
    print("a is a list")

a = {"a": 1}
if isinstance(a, dict):
    print("a is a dictionary")

a = False
if isinstance(a, bool):
    print("a is a boolean")

a= Nigeria
if isinstance(a, str):
    print("a is a string")

a = {'Inyene', 'Python', 'Germany'}
if isinstance(a, set):
    print("a is a set")