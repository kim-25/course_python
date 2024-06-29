"""
Implement the Collatz Conjecture: Start with a number n, and repeatedly apply the rule n → n/2 if n is even
or n → 3n + 1 if n is odd. Print the sequence until n becomes 1.
"""
n = int(input('Enter a number: '))

while n:
    if n % 2 == 0:
        while n:
            div = n/2
            print(div)
            break
    else:
        d = n*3+1
        print(d)
    break




