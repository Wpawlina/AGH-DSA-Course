from zad4testy import runtests
import copy

def capacity(b):
    return b[0]*(b[2]-b[1])
def price(b):
    return b[3]

def select_buildings(T,p):
    T2=copy.deepcopy(T)
    T.sort(key=lambda x:x[2])
    n=len(T)
    F=[[-float('inf') for _ in range(p+1)] for _ in range(n)]
    P=[[None for _ in range(p+1)] for _ in range(n)]
    for k in range(price(T[0]),p+1):
        F[0][k]=capacity(T[0])
    for i in range(1,n):
        for k in range(p+1):
            if price(T[i])<k:
                best=capacity(T[i])
                parent=None
                for j in range(i):
                    if T[j][2]<T[i][1]:
                        if best<F[j][k-price(T[i])]+capacity(T[i]):
                            best=F[j][k-price(T[i])]+capacity(T[i])
                            parent=(j,k-price(T[i]))
                F[i][k]=best
                P[i][k]=parent
    best=-float('inf')
    index=-1
    mprice=-1
    for i in range(n):
        for k in range(p+1):
            if best<F[i][k]:
                best=F[i][k]
                index=i
                mprice=k
    res=[]
    while P[index][mprice] is not None:
        res.append(index)
        index,mprice=P[index][mprice]  
    res.append(index)
    res.reverse
    for r in range(len(res)):
        j=T2.index(T[res[r]])
        res[r]=j
    return  res










runtests( select_buildings )