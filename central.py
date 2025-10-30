import numpy as np
import matplotlib.pyplot as plt

s1 = 1
s2 = 0.5
s3 = 0.1
n1 = int(4/s1)+1
n2 = int(4/s2)+1
n3 = int(4/s3)+1
d1 = []
d2 = []
d3 = []

x1 = np.linspace(-2,2, n1)
x2 = np.linspace(-2,2, n2)
x3 = np.linspace(-2,2, n3)
xA = np.linspace(-2,2, 100)

def func(x):
    return 2 + 0.75*np.tanh(2*x)
for i in range(n1):
    if i+1 == n1 or i+1 == 1:
        continue
    else:
        d1.append((func(x1[i+1])-func(x1[i-1]))/(x1[i+1]-x1[i-1]))
for i in range(n2):
    if i+1 == n2 or i+1 == 1:
        continue
    else:
        d2.append((func(x2[i+1])-func(x2[i-1]))/(x2[i+1]-x2[i-1]))
for i in range(n3):
    if i+1 == n3 or i+1 == 1:
        continue
    else:
        d3.append((func(x3[i+1])-func(x3[i-1]))/(x3[i+1]-x3[i-1]))
        
def funcprime(x):
    return (3/2)*(1/np.cosh(2*x))**2

plt.plot(x1[1:-1],d1, label='1')
plt.plot(x2[1:-1],d2, label='0.5')
plt.plot(x3[1:-1],d3, label='0.1')
plt.plot(xA, funcprime(xA), linestyle='--')
plt.legend(title='Step Size')
plt.show()
