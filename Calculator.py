n = int(input("How many Calculations:"))

for i in range(n):
    print("Calculation:",i+1)

    number1 = float(input("Enter Number1:"))
    number2 = float(input("Enter Number2:"))
    operator = input("Enter Operator:")

    if operator=="+":
        print("Result:",number1+number2)
    elif operator=="-":
        print("Result:",number1-number2)
    elif operator=="*":
        print("Result:",number1*number2)
    elif operator=="/":
        if number2!=0:
            print("Result:",number1/number2)
        else:
            print("Cannot be divided by zero")
    else:
        print("invalid operator")
