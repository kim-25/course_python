#Import the math module (as you want)
import math
from math import *

# Make the Poisson distribution. The user must enter the parameters. Then print out the result
# l = bool(input('Enter a lambda value:  '))
# x = bool(input('Enter a x value:   '))
# p = ((l^x)/(factorial(x)))*exp(-l)
# print(p)

# Make an iterable with some numbers to calculate the product of all those numbers

a = [1,2,3,4,5]
print(math.prod(a))
# From two iterables, calculate the sum of the product of values
r = [1,2,3,4]
s = [5,6,7,8]
print(math.sumprod(r,s))

# Calculate the GCD of two numbers that user gives
# n1 = int(input('Enter a number 1:  '))
# n2 = int(input('Enter a number 2:  '))
#
# print(math.gcd(n1,n2))


# Make the binomial distribution. The user must enter the values: n, x, p. Then print out the result
# n = bool(input('Enter a n value:  '))
# x = bool(input('Enter a x value:  '))
# p = bool(input('Enter a p value:  '))
# c = math.comb(n,x)
#
# pr = c*(p**x)*((1-p)**(n-x))
# print(pr)


# The user enter a float number, and then the ceiling of that number must appear in the screen, as
# "the ceiling of x is y "


# Choose two functions from the math documentation to make exercises like the previous