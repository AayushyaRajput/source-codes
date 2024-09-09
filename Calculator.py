#calculator
operator = input(" what you wanna choose ( + - / *) ")
l1 = float(input("write the number: "))
l2 = float(input("write the number: "))

if operator == "+":
    result = l1+l2
    print(result)

elif operator == "-":
    result = l1 - l2
    print(result)

elif operator == "/":
    result = l1/l2
    print(result)
elif operator == "*":
    result = l1*l2
    print(result)

else:
    print(f"{operator} is not valid")