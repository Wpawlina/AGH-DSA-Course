import random

def krotnosc(num):
    D=[0]*10
    while num!=0:
        dig=num%10
        num//=10
        D[dig]+=1
    jk=0
    wk=0
    for i in range(10):
        if D[i]==1:
            jk+=1
        elif D[i]>1:
            wk+=1
    return jk,wk

def countingSort(T,k,indeks):
    n=len(T)
    C=[0]*k
    B=[None]*n
    for i in range(n):
        C[T[i][indeks]]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(n-1,-1,-1):
        B[C[T[i][indeks]]-1]=T[i]
        C[T[i][indeks]]-=1
    for i in range(n):
        T[i]=B[i]


def radixSort(T):
    n=len(T)
    k=2
    for i in range(k-1,0,-1):
        countingSort(T,10,i)




def pretty_sort(T):
    n=len(T)
    for i in range(n):
        jk,wk=krotnosc(T[i])
        T[i]=[T[i],jk,wk]
    radixSort(T)
    for i in range(n):
        T[i]=T[i][0]


n=100
T=[0]*n
for i in range(n):
    T[i]=random.randint(0,n*n) 
print(T)
print("======")
pretty_sort(T)  
print(T)