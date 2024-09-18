import math
import random

def insertionSort(T):
    n=len(T)
    for i in range(1,n):
        k=i-1
        pom=T[i]
        while k>=0 and T[k]>pom:
            T[k+1]=T[k]
            k-=1
        T[k+1]=pom

def partition(T,L,P):
    pivot=T[(L+P)//2]
    i=L
    j=P
    while i<=j:
        while T[i]<pivot:
            i+=1
        while T[j]>pivot:
            j-=1
        if i<=j:
            T[i],T[j]=T[j],T[i]
            i+=1
            j-=1
    return i,j

def quickSort(T,L,P):
    stos=[]
    stos.insert(0,(L,P))
    while len(stos)>0:
        L,P=stos.pop(0)
        if L<P:
            i,j=partition(T,L,P)
            if j-L>P-i:
                stos.insert(0,(i,P))
                stos.insert(0,(L,j))  
            else:
                stos.insert(0,(L,j))
                stos.insert(0,(i,P))




def bucketSort(T,minE,k):
    n=len(T)
    B=[[]for _ in range(n+1)]
    for i in range(n):
        indeks=math.floor(((T[i]-minE)/k)*n)
        B[indeks].append(T[i])
    for bucket in B:
        b=len(bucket)
        if(b<10):
            insertionSort(bucket)
        else:
            quickSort(bucket,0,b-1)

    C=[]
    for bucket in B:
       C.extend(bucket)
    for i in range(n):
        T[i]=C[i]
   




T=[0]*100
minE=0
k=8
for i in range(100):
    T[i]=minE + int(random.random()*k*100)/100
minE=min(T)
k=int(max(T)-minE+1)
bucketSort(T,minE,k)
print(T)




