import random


#my_list = ['sin', 'cos', 'tan','f(x)', 'g(x)']
#print(my_list)
#my_list[0] = 'sin(x)'
#print(my_list)
#my_list[1] = 'cos(x)'
#print(my_list)
#my_list[2] = 'tan(x)'
#print(my_list)



#############
#
#my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
#print(my_list)
#my_list[0:3] = ['sin(x)', 'cos(x)', 'tan(x)']
#print(my_list)

###########
#my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
#print(my_list)
#my_list[0:5:2] = ['sin(x)', 'cos(x)', 'tan(x)']
#print(my_list)

##########3
#my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
#del [my_list]
#print(my_list)
#del my_list[0:3]
#print(my_list)

############################01-abril
#my_tuple = (object)
#my_tuple = (1,2,3)
#my_tuple[0] = 0

#Verify

#age = int(input('What is your age?:  ')) #type casting para la conversion a los tipos de datos
#if age < 18:
 #   print('Your are a kid')
#else:
  #  print('your are an adult')

#x = 'spam'
#while x:
    #print (x, end=' ')
    #x = x[1: ]

#x = 10
#while x:
 #   x -= 1
  #  if x % 2 == 0:
   #     continue
        # pass
   # print

#k = 0
  # while k<5:
   #    print(f'The value of k is {k}')
    #   k =+ 1

#x = 'spam'
#while x:
 #   print(x, end=' ')
  #  x = x[1: ]

#x = 10
#while x:

 #   x -= 1
  #  if x % 2 == 0:
   #     continue
    #print(x)

#while True:
 #   name = input('Enter your name:  ')
  #  if name == 'stop':
   #     break
    #age = input('Enter your age:  ')
 #   print('Hello', name, '=>', int(age)**2)
#
#print('Out of while')

#words = ['despair ', 'phone', 'computer','english']
#k = -len(words)
#while words:
 #   print(words[k])
  #  del words[k]
   # k += 1
    #print(words)

#for letter in words:
 #   print(letter)

#for letter in range(0, len(words)):
 #   print(word[index])

#List Manipulation

# summ = 0
# while True:
#     num = int(input('Enter a number: '))
#     if num <0:
#         print(summ)
#         break
#
#     summ += num

# items = ['aaa', 111, (4,5), 2.01]
# tests = [(4,5), 3.14]
# for key in tests:
#     for item in items:
#         if items:
#             if item == key:
#                 print (key, 'was found')
#                 break
#             else:
#                 print(key, 'was not found')

# seq1 = 'Mood'
# seq2 = 'Spivak'
# res = []
# for x in seq1:
#     if x in seq2:
#         res

# a, b = 2, 3 #Pythonic
# for _ in range (5):
#     if _ == a:
#         print(_, a)
#         break
#     elif _ == b: print('This is b')
#     else: print('nothing')
# print('Nothing')
# print('jejeje')
#Summ of positive numbers
#Objetive: Write a programm that repaetly asks

#List manipulation with user input
#Objective: Create a program  that allows the user to build a list of even numbers, if the user enters an add number
# skip adding it to the list
#
# lista = []
# while True:
#     cont = bool(int(input('Do you want to continue?: 1 yes. 0 no')))
#     if not cont:
#         break
#     num = int(input('Enter a number: '))
#     if num % 2 == 0:
#         lista.append(num)
# print(lista)

#Pasword checker
#Obhective: Write a program that repeatedly asks the user to enter a pasword.
#Stop asking when the correct pasword ('python123') is entered

# while True:
#     pasword = 'python123'
#     num = input('Enter a pasword:  ')
#     if num ==pasword:
#         print('The pasword is correct')
#         break

"""
factorial calculation
objective: write a program to calculate the factorial of given number
"""

# n = int(input('Enter a number:  '))
# fac = 1
# if n == 1 or 0:
#     print(f'the factorial is {fac}')
# else:
#     for s in range (1,n + 1):
#         fac = fac * s
#     print(f'The factorial is {fac}')

# # people = ['F1', 'F2','A1', 'A2', 'A3','S1', 'S2', 'S3', 'S4' ]
# #
# # fellow = ['F1', 'F2']
# # associates = ['A1', 'A2', 'A3']
# # students = ['S1', 'S2', 'S3', 'S4']
#
# pos_result = []

# for m1 in people:
#     for m2 in people:
#         for m3 in people:
#             pos_result.append((m1,m2,m3))
#             #print(m1, m2, m3)
#
#
# print(len(pos_result))

#iteration: proceso de ir a traves de los elementos de una coleccion
# iterable: es un objeto con metodo iter, podemos usar el [], paraobtener los eleementos de un objeto
#iterator: objeto con un __next_- method
#
# names = ['Hamilton', 'Checo', 'Leclerc']
# teams = ['Mercedes', 'Redbull', 'Ferrari']
#
# # for n, t in zip(names, teams):
# #     print(n,t)
# for n, t in zip(names, teams):
#     print(n.upper())

# for name in zip(names, teams):
#     print(name[0])

# print(dir(zip('aaa', (1,2,3))))
# a = range(2,10)


# for num in a:
#     print(num)

# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# #print(dir(enumerate(seasons)))
#
# for _ in enumerate(seasons):
#     print(_[1])

# s = 'cat'

x = 0


# def increment_by_n(n):
#     x = 0
#     x += n
#     return x
#
#
# print(x,increment_by_n(5))
# print(x)

x=0

# def increment_by_2n(n):
#     return 2*n
#     x += increment_by_2n(5)
# # print(x,increment_by_n(5))
# print(x)

# complex(real = 0, imag=0) #from doc
# complex(4,5) #4 + 5j using positional
# complex(5,4) #5+4j using positional
# complex(imag=5, real=4) #4+5j using kw

#una libreria es un conjunto de modulos
#un modulo tiene fuciones, clases y variables
#paqueteria tiene modulos relacionados

#
# names= ('jacke','esteban','fred', 'tim')
#
# corrected_names = map(lambda name: name.title(), names) #iterator
#for item in corrected_names:
#print(item)
#
# print(list(corrected_names))
#
# for item in map(lambda x, y,z: 2*x**y/z,[1,2,3],[0.1,0.2,0.3],[1,2]):
#     print(item)

# grades = [
#     ('linear algebra', 8.8),
#     ('differential calculus',2.0),
#     ('actuarial calculus ll', 9.4),
#     ('probabilities theory', 1.0)
# ]
# test = lambda grad: grad[1]>=3
# x= filter(test,grades)
# print(list(x))

# def f(*args):
#     print(args)
#
# f(5,7,8,9,10)

# def my_func(*numbers, **letters):
#     return numbers, letters
#
#
#
# a = my_func(*numbers: 5,7,9,20,54, a=1, b=5)
# print(a[1]['b'])


# my_range = range(7)
# print(my_range)
# print(*my_range)
# my_list = [1, 2, 3, 4]
# print(*my_list)
# print(*range(7))

# days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday'] # Packing
# a, b, c, d, e = days
# print(a)
# *rest, school, free = days
# print(rest)
# print(school)

#Importr librerias
# import numpy
# e = numpy.pe
#
# print(e)

#renombrar la libreria
# import numpy as np


#para instalar librerias nos vamos a la terminal y ponemos pip install nombre de la paqueteria

#importar algo especificamente
# from numpy import e, pi
# print (e)

# accendemos a las funciones de la libreria
# import math
# print(math.sin())

# Para importar todo lo de la libreria
#
# from math import *

# random.seed()
# print(random.random())
# print(random.random())
# print(random.random())

##creamos funcines
def









