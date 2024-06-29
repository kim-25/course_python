import statistics

"""
A pharmaceutical company wants to know whether an experimental drug affects systolic blood pressure.
Fifteen randomly selected subjects were given the drug and, after sufficient time for the drug to have an impact,
their systolic blood pressures were recorded.
The data appears in a python list.

THE FOLLOWING POINTS MUST BE DONE USING SOME FUNCTIONS OF SOME MODULE, AND WITH ANOTHER FUNCTION THAT YOU BUILT,
THAT IS, IMITATE THE BEHAVIOUR OF THAT FUNCTION

1. Calculate the value of 'x bar' (sample mean) and the value of s (the sample standard deviation)

"""

data = [172, 140, 123, 130, 115, 148, 108, 129, 137, 161, 123, 152, 133, 128, 142]

#con las funciones del modulo
print(statistics.mean(data))
print(statistics.stdev(data))
#con mis funciones
##media
n=len(data)
m = sum(data)/n
print(m)

##desviacion estandar
d=0
r2=0
for s in data:
    d = (s-m)
    de = d ** 2
    r2 = r2 +de
    p = r2 / (n-1)
    ds = p ** 0.5
print(ds)

