def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(T,n,i):
    maxIndex=i
    l=left(i)
    r=right(i)
    if l<n and T[l]>T[maxIndex]:
        maxIndex=l
    if r<n and T[r]>T[maxIndex]:
        maxIndex=r
    if maxIndex!=i:
        T[i],T[maxIndex]=T[maxIndex],T[i]
        heapify(T,n,maxIndex)

def buldHeap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T,n,i)

def heapSort(T):
    n=len(T)
    buldHeap(T)
    for i in range(n-1,0,-1):
        T[0],T[i]=T[i],T[0]
        heapify(T,i,0)
T = [4, 2, 7, 1, 9, 3, 5]

heapSort(T)
print(T)


    