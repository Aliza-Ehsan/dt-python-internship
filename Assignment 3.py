import numpy as np
from sklearn.linear_model import LinearRegression
import statistics
import sympy as sp
import matplotlib.pyplot as plt

# Step 1: Ask for user's name, age, and favorite number
name = input("Please Enter your name: ")
age = int(input("Please Enter your age: "))
favorite_number = int(input("Now Enter your most favorite number: "))

# Step 2: Generate a random array and calculate mean, median, and standard deviation
random_array = np.random.randint(1, 100, size=10)
mean = np.mean(random_array)
median = np.median(random_array)
std_dev = np.std(random_array)

print(f"Random array: {random_array}")
print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")

# Step 3: Create a simple linear regression model
X = np.array([[age]]).reshape(-1, 1)
y = np.array([favorite_number])

reg_model = LinearRegression()
reg_model.fit(X, y)
predicted_fav_number = reg_model.predict([[age]])

print(f"Linear Regression: Predicted favorite number for age {age} is {predicted_fav_number[0]}")

# Step 4: Since correlation needs at least two data points, we won't calculate it with only one.
print("Correlation can't be calculated with a single data point. Skipping correlation calculation.")

# Step 5: Conditional checks for age
if age < 18:
    print("You're a minor!")
elif age == 21:
    print("You're 21, congratulations!")
else:
    print("You're an adult!")

# Step 6: Generate prime numbers up to 100
primes = []
for num in range(2, 101):
    if sp.isprime(num):
        primes.append(num)

print(f"Prime numbers up to 100: {primes}")

# Step 7: Create a simple plot of age vs favorite number
plt.plot(age, favorite_number, 'bo', label=f'Age: {age}, Favorite Number: {favorite_number}')
plt.title("Age vs. Favorite Number")
plt.xlabel("Age")
plt.ylabel("Favorite Number")
plt.legend()
plt.grid(True)
plt.savefig("Age_vs_favorite_number.png")  # Save the plot as a file
plt.show()  # Display the plot
