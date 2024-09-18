from zad3testy import runtests
from queue import PriorityQueue

def isPossible(a,b):
    A=[False]*10
    B=[False]*10
    while a>0:
        A[a%10]=True
        a//=10
    while b>0:
        B[b%10]=True
        b//=10
    for i in range(10):
        if A[i] and B[i]:
            return True
    return False

    
    



def find_cost(P):
    n=len(P)
    F=[float('inf') for _ in range(n)]
    _min=float('inf')
    _max=-float('inf')
    s=-1
    t=-1
    for i in range(n):
        if P[i]<_min:
            _min=P[i]
            s=i
        if P[i]>_max:
            _max=P[i]
            t=i
    F[s]=0
    def f(i):
        nonlocal F
        for j in range(n):
            if i!=j and  isPossible(P[i],P[j]) and abs(P[i]-P[j]) + F[i] < F[j]:
                F[j]=abs(P[i]-P[j]) + F[i]
                f(j)
    f(s)
    return F[t] if F[t]<float('inf') else -1 


    

runtests(find_cost) 
