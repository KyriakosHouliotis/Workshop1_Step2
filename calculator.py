operator = input("Operator (+, -, x, /):\n")
num1 = input("First Number:\n")
num2 = input("Second Number:\n")

num1 = int(num1)
num2 = int(num2)


if operator == "+":
    out =  num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "x":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2
    
print("Answer: " + str(out))