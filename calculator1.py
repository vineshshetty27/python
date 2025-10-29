num1 = float(input("Enter first no: "))
num2 = float(input("Enter second no: "))
op = input("Enter operation (+, -, *, /, %): ")
match op:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        result = num1 / num2
    case '%':
        result = num1 % num2
print("Result:", result)
