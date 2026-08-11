import art



print("Welcome to Project Calculator!")

def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(art.logo)
    number1 = float(input("Enter first number: \n"))

    should_accumulate = True

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter operation that you want to use: \n")
        number2 = float(input("Enter second number: \n"))

        answer = operations[operation_symbol](number1, number2)
        print(f"{number1}{operation_symbol}{number2} = {answer}")

        choice = input(f"Type 'y' to continue  calculating with {answer},or type 'n' to start a new calculation ,"
                       f"Type 'e' to end calculating with calculator \n").lower()

        if choice == "y":
            number1 = answer
        elif choice == "n":
            should_accumulate = False
            print("\n" *50)
            calculator()
        else:
            print("Thank you for using this program")
            should_accumulate = False

calculator()