#approximation of the number Pi

import math

print("Enter a positive integer value for k which equals the number of sums you want to approximate the number PI. \nThe bigger k is, the better the approximation: ")

k = None
while k is None or k < 0:
    try:
        k = int(input())
    except ValueError:
        print("The number you put in is not a proper input for k. Try a positve integer!")

total = 0

for i in range(k):
    term = (math.factorial(4*i)*(1103+26390*i))/(pow(math.factorial(i),4)*pow(396,4*i))
    total += term

ApPi = 1/(((2*math.sqrt(2))/9801)*total)

print("Your approximation is: ", ApPi)

error = 100*(ApPi-math.pi)/math.pi

print(f"... which is a percentage error of: {error:.50f}%.")
