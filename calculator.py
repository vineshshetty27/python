def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error Division by zero."
print("Calculator")
print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")
ch = input("Enter ch: ")
num1 = float(input("Enter first no: "))
num2 = float(input("Enter second no: "))
if ch == '1':
    print("Result:", add(num1, num2))
elif ch == '2':
    print("Result:", subtract(num1, num2))
elif ch == '3':
    print("Result:", multiply(num1, num2))
elif ch == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")
