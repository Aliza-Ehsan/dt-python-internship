# Library for generating random numbers
import random

# Function to add two numbers
def add(p, q):
    return p + q

# Function to subtract two numbers
def sub(p, q):
    return p - q

# Function to multiply two numbers
def mul(p, q):
    return p * q

# Function to divide two numbers
def div(p, q):
    if q != 0:
        return p / q
    else:
        return "Error! Division by zero."

# Function to calculate the derivative of ax^n
def derivative(a, n):
    return f"{a * n}x^{n-1}"

# Function to calculate the integral of ax^n
def integral(a, n):
    return f"{a / (n+1)}x^{n+1} + C"

# Function to simulate a dice roll
def roll_dice():
    return random.randint(1, 6)

# Function to perform arithmetic operations
def calculator(tries):
    while tries > 0:
        print(f"\nYou have {tries} calculation tries remaining.")
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Derivative ")
        print("6. Integral ")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {sub(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {mul(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {div(num1, num2)}")
        
        elif choice == '5':
            a = float(input("Enter the coefficient (a): "))
            n = float(input("Enter the power of x (n): "))
            print(f"The derivative of {a}x^{n} is: {derivative(a, n)}")

        elif choice == '6':
            a = float(input("Enter the coefficient (a): "))
            n = float(input("Enter the power of x (n): "))
            print(f"The integral of {a}x^{n} is: {integral(a, n)}")

        else:
            print("Invalid input. Please select a valid operation.")
        
        tries -= 1

        if tries > 0:
            print(f"\nYou have {tries} calculation tries left.")
        else:
            print("You have used all your calculation tries.")

# Main function to handle the game and calculator
def main():
    print("Welcome to the Dice Game! 🎲")
    print("You must roll the dice to earn calculation tries.")
    
    while True:
        roll = input("\nDo you want to roll the dice? (yes/no): ").lower()
        if roll == 'yes':
            points = roll_dice()
            print(f"\nYou rolled a {points}. You have {points} calculation tries.")
            calculator(points)
        elif roll == 'no':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

# Run the main function
main()