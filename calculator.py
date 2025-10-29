# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


def main():
    print("===== Simple CLI Calculator =====")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit.")
    
    while True:
        choice = input("\nEnter operation (+, -, *, /) or 'exit' to quit: ").strip().lower()
        
        if choice == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        
        if choice not in ['+', '-', '*', '/']:
            print("Invalid operation. Please choose from +, -, *, /.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '+':
            result = add(num1, num2)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)

        print(f"Result: {result}")

if __name__ == "__main__":
    main()
