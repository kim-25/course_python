# For each point, use the print() function

# 1. Use 'in' operator to obtain a True value
print('5' in '512')

# 2. Use not in operator to obtain a True value
print('5' not in '12')
# 3. Use * operator with a string (as you want)
print('.py'*2)
# 4. Use + operator with a string and with a list(as you want)
print('hello' * '' *'world')
# ------------------- Slicing for strings-----------------------
# We can use s[i:j:k] to make a slicing in python, solve each point

# 5. From the sentence, print out "is a logical consequence of the axioms and previously proved theorems"
sentence = """In mathematics, a theorem is a statement that has been proved, or can be proved. The proof of a theorem 
is a logical argument that uses the inference rules of a deductive system to establish that the theorem 
is a logical consequence of the axioms and previously proved theorems."""
index = sentence.rindex('is')
print(index)
print(sentence[index:])


# 6.From the user's input, print the name, but beginning with the last names. Make sure each first letter is capitalized
# sheldon axler -> Axler Sheldon
name = input('What is your full name? ').title() #UNCOMMENT WHEN YOU USE THIS
my_split = name.split()
print(my_split)
print(my_split[-1], my_split[0])
# 7. 'tcerroc eht tuo tnirp dna ti esrever tsuJ .od ot deen uoy tahw tuoba tnih a uoy evig ot ecnetnes a tsuj si sihT'

print('tcerroc eht tuo tnirp dna ti esrever tsuJ .od ot deen uoy tahw tuoba tnih a uoy evig ot ecnetnes a tsuj si sihT'[::-1])
# 8. The frog jump two letters in the mot string. What is the final string?
mot = 'you are doing well. Do not doubt on you!'
print(mot[::2])
# 9. From the sentence variable, how many characters are in there?
print(len(sentence))