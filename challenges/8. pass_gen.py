import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

pw = [ ]
ln = [ ]
nn = [ ]
sn = [ ]

print("Welcome to the pasword generator")
l = int(input("How many letters would you like in you pasword?:  "))
n = int(input("How many numbers would you like in you pasword?:  "))
s = int(input("How many simbols would you like in you pasword?:  "))


def password(a,b,c):
    lista = []

for _ in range(0,l):
    lr = random.choice(letters)
    ln += ln + lr
    print(ln)

for _ in range(0,n) :
    nr = random.choice(numbers)
    nn += sn + nr
    print(nn)

for _ in range(0,s) :
    sr = random.choice(symbols)
    sn += sn + sr
    print(sn)

print(f'Here is your pasword: {p}')