# Generate and print the multiplication table (up to 10) for a given number
r = int(input('Enter a number:  '))
for s in range (1,11):
    m = r*s
    print(f'{r} x {s} = {m}')


