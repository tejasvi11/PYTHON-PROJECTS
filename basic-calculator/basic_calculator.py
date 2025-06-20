def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Cannot divide by zero!"
    return a / b

while True:
    print("\nSimple Calculator")
    print("Choose operation: +, -, *, /")
    print("Type 'q' to quit")

    choice = input("Enter operation: ")

    if choice == 'q':
        print("Goodbye! 👋")
        break

    if choice in ['+', '-', '*', '/']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print("Result:", add(num1, num2))
        elif choice == '-':
            print("Result:", subtract(num1, num2))
        elif choice == '*':
            print("Result:", multiply(num1, num2))
        elif choice == '/':
            print("Result:", divide(num1, num2))
    else:
        print("❌ Invalid operation. Try again.")
