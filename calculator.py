try:
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))

    print("enter the operation to perform:\nPress + to addition\nPress - to subtraction\nPress * to multiplication\nPress / to divide\n Press ** to power")
    op=input("enter the operation: ")
    match op:
        case "+":
            print(f"The result is {a+b}")
        case "-":
            print(f"The result is {a-b}")
        case "*":
            print(f"The result is {a*b}")
        case "/":
            print(f"The result is {a/b}")
        case "**":
            print(f"The result is {a**b}")
except Exception as e:
    print("enter a valid value of a and b")