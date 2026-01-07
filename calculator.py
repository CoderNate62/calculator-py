import sys
import math

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return math.pow(a, b)

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        return math.sqrt(a)

    def log(self, a):
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        return math.log(a)

    def sin(self, a):
        return math.sin(a)

    def cos(self, a):
        return math.cos(a)

    def tan(self, a):
        return math.tan(a)

def main():
    calc = Calculator()
    print("Welcome to Python Calculator")
    print("Operations: +, -, *, /")
    print("Enter 'q' to quit")

    while True:
        user_input = input("\nEnter calculation (e.g., 2 + 2): ").strip()
        
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
            
        try:
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Please use: number operator number")
                continue
                
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
            
            result = 0
            if operator == '+':
                result = calc.add(num1, num2)
            elif operator == '-':
                result = calc.subtract(num1, num2)
            elif operator == '*':
                result = calc.multiply(num1, num2)
            elif operator == '/':
                result = calc.divide(num1, num2)
            else:
                print(f"Unknown operator: {operator}")
                continue
                
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
