import random

f = input('Choose your position:  paper(p), scissors (s) or rock(r):   ')

if f




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

c = ['p','s','r']
x = random.choice(c)
p = paper
f = input('Choose your position:  paper(p), scissors (s) or rock(r):   ')

if f == x:
    print('win')
