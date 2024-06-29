"""A word is a palindrome if is identical forward and backward, for example anna, civic, lever, hannnah are
all examples of palindromic words.
Write a program that treads a word from the user to determine whether it is a palindrome.
Display the result, including
a meaningful output message"""

def is_palindrome(wr):
    wr = wr.lower()
    #wr = wr.replace(" ","")
    return wr == wr[::-1]
def main():
    wr = str(input('Enter a word:  '))
    if is_palindrome(wr):
        print("This is palindrome :)")
    else:
        print("This is not a palindrome")

if __name__ == "__main__":
    main()

