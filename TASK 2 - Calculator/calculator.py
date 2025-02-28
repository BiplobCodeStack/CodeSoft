
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Simple Calculator")
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            print("Choose the operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "1":
                result = add(num1, num2)
                print(f"The result of addition: {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"The result of subtraction: {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"The result of multiplication: {result}")
            elif choice == "4":
                result = divide(num1, num2)
                print(f"The result of division: {result}")
            elif choice == "5":
                break
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter numerical values.")

if __name__ == "__main__":
    main()
