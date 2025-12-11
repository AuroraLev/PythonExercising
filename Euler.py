#approximation of the Euler Number

import math

n = None
while n is None:
    try:
        n = int(input("Enter an integer value n which equals to the number of iterations you want to approximate the Euler number e. \nThe bigger n is, the better the approximation: "))
    except ValueError:
        print("The number you put in is not an integer number.")

ApEuler = pow(1+(1/n),n)

print("Your approximation is: ", ApEuler)

error = abs(100*(ApEuler - math.e)/math.e)

print(f"... which is a percentage error of: {error:.5f}%.")