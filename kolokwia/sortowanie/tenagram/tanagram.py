from zad1testy import runtests
from queue import Queue



def tanagram(x, y, t):
    n=len(x)
    X=[Queue() for _ in range(26)]
    for i in range(n):
        X[ord(x[i])-ord('a')].put(i)
    for i in range(n):
        pos=X[ord(y[i])-ord('a')].get()
        if abs(pos-i) > t: 
            return False
    return True


   


runtests(tanagram)