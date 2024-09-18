
from functools import cache
import math
import sys
sys.set_int_max_str_digits(10000000)

def fib_rek1(n):
    if n<=1:
        return 1
    return fib_rek1(n-1)+fib_rek1(n-2)


@cache
def fib_rek2(n):
    if n<=1:
        return 1
    return fib_rek2(n-1)+fib_rek2(n-2)

def fib_iter(n):
    F=[0]*(n+1)
    F[0]=1
    F[1]=1
    for i in range(2,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]
def fib_const(n):
    return (1/math.sqrt(5))*pow((1+math.sqrt(5))/2,n)-(1/math.sqrt(5))*pow((1-math.sqrt(5))/2,n)


print(fib_const(100))
    