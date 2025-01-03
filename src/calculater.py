while 6 > 5:
    operator = input("Enter an operator (+ - * / ): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print(round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print(round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print(round(result, 3))
    elif operator == "/":
        if num2 == 0:
            print("Can't divide by 0")
        else:
             result = num1 / num2
             print(round(result, 3))
    else:
        print(f"{operator} is not a valid operator")
    askagain = input("Would you like to use this calculator again? (type 1 if you want to keep using) ")
    if askagain  != "1":
        break