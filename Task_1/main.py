a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print(f"The addition of {a} and {b} is {a + b}")
print(f"The multiplication of {a} and {b} is {a * b}")
print(f"The subtraction of {b} from {a} is {a - b}")
if b != 0:
    print(f"The division of {a} by {b} is {a / b}")
else:
    print(f"The Second number cannot be a 0 for division")