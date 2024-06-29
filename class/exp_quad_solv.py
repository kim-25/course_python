"""
Write a lambda function that calculates the roots of a quadratic equation ax^2+bx+c=0.
Assume that the discriminant is always non-negative.
"""
a= input(int('Enter a quadratic term:  '))
b= input(int('Enter a lineal term:  '))
c= input(int('Enter a  independent term:  '))

x1= (-b + ((b**2)-4*a*c)**0.5)/2*a
x2= (-b - ((b**2)-4*a*c)**0.5)/2*a
print(f'x1 = {x1}')
print(f'x2 = {x2}')
#

