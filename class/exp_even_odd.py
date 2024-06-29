# Make a program that determines if a number (given by the user) is odd or even
#solicitar el numero de usuario
number = int(input('Enter a number: '))
#evaluar si es par o impar
if number % 2 == 0 :
    print(f'{number} is even')
else:
    print(f'{number} is odd')
#imprimir el resultado
