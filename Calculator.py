def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def undo(result_list):
    result_list.pop()
    return result_list[-1]

def main():
    result = 0
    result_list = [0]
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Undo")
        print("6. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = addition(a, b)
            result_list.append(result)
            print("Result:", result)
        elif choice == 2:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = subtraction(a, b)
            result_list.append(result)
            print("Result:", result)
        elif choice == 3:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = multiplication(a, b)
            result_list.append(result)
            print("Result:", result)
        elif choice == 4:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = division(a, b)
            result_list.append(result)
            print("Result:", result)
        elif choice == 5:
            if len(result_list) > 1:
                result = undo(result_list)
                print("Result:", result)
            else:
                print("No operations to undo.")
        elif choice == 6:
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()

