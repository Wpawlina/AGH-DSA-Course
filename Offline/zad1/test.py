
from zad1testy import  runtests
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def SortH2(p,k):
    L=Node()
    L.next=p # stworzenie wartowanika dla listy początkowej 
    H=Node() # stworzenie listy wynikowej wraz z wartownikiem
    new=H   # wskaznik na poczatek listy wynikowej 
    while L.next is not None:
        minP=L
        i=0
        q=L.next
        while q.next is not None and i<k:   # wyszukiwanie elementu minimalnego w podliscie o dlugosic k znajdujacej sie po elemencie sprawdzanym
            if q.next.val<minP.next.val:
                minP=q
            q=q.next
            i+=1
        if minP.next.val<L.next.val: # jesli element minmalny jest mniejszy od elementu sprawdzanego, przepinam element sprawdzany na miejsce elementu minimalnego a element minimalu dołaczam do listy wynikowej
            element=minP.next
            H.next=element
            H=H.next
            minP.next=L.next
            temp=L.next.next
            minP.next.next=element.next
            L.next=temp
        else:               # w przeciwym wypadku dołaczam do listy wynikowej element sprawdzany odpinajac go od listy początkowej 
            H.next=L.next
            H=H.next
            L.next=L.next.next  
    return new.next # zwracam liste wynikową bez wartownika


def tableify(L,n):
    T=[0 for _ in range(n)]
    i=0
    while L.next is not None:
        T[i]=L.next
        i+=1
        L=L.next
    return T  

def linkedListLength(L):
    n=0
    while L.next is not None:
        n+=1
        L=L.next
    return n

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(T,n,i):
    minIndex=i
    l=left(i)
    r=right(i)
    if l<n and T[l].val<T[minIndex].val:
        minIndex=l
    if r<n and T[r].val<T[minIndex].val:
        minIndex=r
    if minIndex!=i:
        T[i],T[minIndex]=T[minIndex],T[i]
        heapify(T,n,minIndex)

def buldHeap(T,n):
    for i in range(parent(n-1),-1,-1):
        heapify(T,n,i)




def SortH(p,k):
    
    L=Node(None)
    L.next=p
    n=linkedListLength(L)
    if k>=n:
        k=n-1
    T=tableify(L,n)
    buldHeap(T,k+1)
    head=L
    for i in range(k+1,n):
        result=T[0]
        T[0]=T[i]
        heapify(T,k+1,0)
        L.next=result
        L=L.next
        L.next=None
    for i in range(k+1):
        L.next=T[0]
        T[0]=T[k-i]
        heapify(T,k-i,0)
        L=L.next
    L.next=None
    return head.next

def printLinkList(L):
    while L.next is not None:
        print(L.next.val,end='->')
        L=L.next

def printtable(T):
    n=len(T)
    for i in range(n):
        print(T[i].val,end=' ')





        







runtests( SortH,True )