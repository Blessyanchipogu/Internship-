while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter Second number: "))
    operation = input("Enter Operation (+, -, *, /): ")

    if operation == "+":
        print(num1 + num2)

    elif operation == "-":
        print(num1 - num2)

    elif operation == "*":
        print(num1 * num2)

    elif operation == "/":
        print(num1 / num2)

    else:
        print("Incorrect operation.")

    another_calc = input("Do you want another calculation (y/n)")

    if another_calc == "y":
        continue
    else:
        break