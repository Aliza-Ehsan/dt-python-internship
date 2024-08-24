#code for a simple calculator

print("select an operation you want to perform")
print("1. ADDITION")
print("2. SUBRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

operation=input()

if operation=="1":
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("The sum of these two numbers is:" , (num1+num2))
elif operation=="2":
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("The difference of these two numbers is:" , (num1-num2))
elif operation=="3":
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("The product of these two numbers is:" , (num1*num2))
elif operation=="4":
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print("The division of these two numbers is:" , (num1/num2))
else:
    print("Invalid Entry")