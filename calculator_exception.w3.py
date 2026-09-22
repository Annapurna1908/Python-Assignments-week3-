class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero!"


calculator = Calculator()

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\n===== CALCULATOR =====")
    print("Addition:", calculator.add(num1, num2))
    print("Subtraction:", calculator.subtract(num1, num2))
    print("Multiplication:", calculator.multiply(num1, num2))
    print("Division:", calculator.divide(num1, num2))

except ValueError:
    print("Please enter numbers only!")