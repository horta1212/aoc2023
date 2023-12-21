
'''
steps = [20,45,65]
max_steps = max(steps)
min_steps = min(steps)

lcm = min_steps
while True:
    lcm += min_steps 
    j=0
    while j < len(steps):
        print('j',j)
        if lcm % steps[j] != 0:
            print('lcm',lcm)
            break
        j += 1

    print(j)
    if j==len(steps):
        break

print('lcm',lcm)
'''
from bryces_utils import Timer
from math import sqrt
def prime_factors(num):
    i = 1
    factor_list=[]
    primes_list=[]
    while num > 1:
        i+=1
        if num % i == 0:
            factor_list.append(i)
            num = num/i
            print(num)
            i=1

    print(factor_list)
    return(factor_list)

#with Timer('sqrt_factors'):
#    prime_factors(1e24)

def prime_numbers(num):
    prime_list=[2]
    for i in range(3,int(num)):
        prime=True
        for prime in prime_list:
            if i % prime == 0:
                prime=False
                break
        if prime:
            prime_list.append(i)
        if i % (num/100) == 0:
            print('i',i)
            print(prime_list)
    return(prime_list)

from copy import deepcopy
def deep_copy(x):
    return(deepcopy(x))

def list_copy(x):
    return([i for i in x])


x = [0,1,2,3,4,5,6,7,8,0]
with Timer('deepcopy'):
    for i in range(10000):
        y = deep_copy(x)

with Timer('list_copy'):
    for i in range(10000):
        y = list_copy(x)

print()

import day17.d17 as d17
from importlib import reload
reload(d17)

loops = 1000000
'''
with Timer('shove'):
    for i in range(loops):
        x = d17.shove(x, x[-1])
    print(x)
    
with Timer('shove2'):
    for i in range(loops):
        x = d17.shove2(x, x[-1])
    print(x)

with Timer('shove3'):
    for i in range(loops):
        x = d17.shove3(x, x[-1])
    print(x)

def test_shove4():
    x = [0,1,2,3,4,5,6,7,8,0]
    for i in range(loops):
        x = d17.shove4(x, x[x[-1]])
    print(x)

with Timer('shove4'):
    test_shove4()


def test_shove_len9():
    x = [0,1,2,3,4,5,6,7,8,0]
    for i in range(loops):
        x = d17.shove_len9(x, x[x[-1]])
    print(x)

with Timer('shove_len9'):
    test_shove_len9()
'''


x=dict()
with Timer('Create entries'):
    for i in range(loops,-1,-1):
        x[i]=i

null = 0
with Timer('Read entries'):
    for i in range(loops):
        null += x[i]

for i in list(x.keys())[0:10]:
    print(i)

import sys
print('dict_size: ', int(sys.getsizeof(x)/1e6), 'e6',sep='')
print(sys.version)
        

        





