ra = range(1,10,2) # using positional-only

#definition a function with positional only

def fun1(value1, value2, value3, /):
    print(value1/value3 + value2)

#ositional or keyword with a built-in

com = complex(imag=5, real=1)
com2 = complex(real=1, imag=5)
com3 = complex(5,4)
com4 = complex(imag=10)
print(com4)

#definition a function with positional or keyword
def func2(r,i=0):
    print(f'{r}+{i}j')

#func2(i=4, r=8)

#keyword only
def func3(pos1, *, live, student = ''):
    print(live + student +str(pos1))

func3(pos1:5, live='True')

def some(obs, k_or_guess,my_iter='20',/, thresh='1e-05',check_finite ='True',*,seed='None'):
    print(obs+k_or_guess+my_iter+thresh+check_finite+seed)

some( 'Hola', 'adios', seed='example')


#func1(value1 =1, value2=5, value3= 10)

