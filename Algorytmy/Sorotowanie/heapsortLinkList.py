class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

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

def printLinkList(L):
    while L.next is not None:
        print(L.next.val,end='->')
        L=L.next

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
    if l<n and T[l].val>T[maxIndex].val:
        maxIndex=l
    if r<n and T[r].val>T[maxIndex].val:
        maxIndex=r
    if maxIndex!=i:
        T[i],T[maxIndex]=T[maxIndex],T[i]
        heapify(T,n,maxIndex)

def buldHeap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T,n,i)

def heapSort(L):
    n=linkedListLength(L)
    T=tableify(L,n)
    buldHeap(T)
    for i in range(n-1,0,-1):
        T[0],T[i]=T[i],T[0]
        heapify(T,i,0)
    L.next=T[0]
    for i in range(n-1):
        T[i].next=T[i+1]
    


linked_list = Node(None)
linked_list.next = Node(5)
linked_list.next.next = Node(17)
linked_list.next.next.next = Node(8)
linked_list.next.next.next.next = Node(1)
linked_list.next.next.next.next.next = Node(3)
linked_list.next.next.next.next.next.next = Node(22)
printLinkList(linked_list)
print("\n--------")
heapSort(linked_list)
printLinkList(linked_list)



