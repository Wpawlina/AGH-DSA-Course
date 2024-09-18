import math
import random

class Node:
    def __init__(self,val):
        self.next=None
        self.val=val


def listLength(L):
    L=L.next
    n=0
    while L is not None:
        n+=1
        L=L.next
    return n
def insert(first,element):
    while first.next is not None and first.next.val < element.val:
        first=first.next
    first.next,element.next=element,first.next
def insertionSort(first):
    a=Node(None)
    while first.next!=None:
        temp=first.next
        first.next=temp.next
        insert(a,temp)
    first.next=a.next
def connectLists(L1,L2):
    while L1.next is not None:
        L1=L1.next
    L1.next=L2.next
    L2.next=None



def Sort(L):
    n=listLength(L)
    B=[None]*n
    for i in range(n):
        B[i]=Node(None)
    while L.next is not None:
        elemnt=L.next
        L.next=L.next.next
        temp=B[math.floor((elemnt.val)//(10/n))].next
        B[math.floor((elemnt.val)//(10/n))].next=elemnt
        elemnt.next=temp
    for i in range(n):
        insertionSort(B[i])   

    for i in range(1,n):
        connectLists(B[0],B[i])
    L.next=B[0].next


def array_to_sentinel_list(array):
    # Tworzenie głowy listy z wartownikiem
    sentinel_head = Node(None)
    current = sentinel_head

    # Dodawanie elementów z tablicy do listy
    for val in array:
        current.next = Node(val)
        current = current.next


    return sentinel_head

# Funkcja do wyświetlania listy z wartownikiem
def display_list_with_sentinel(head):
    current = head
    while current is not None:
        print(current.val, end="->")
        current = current.next


# Przykładowe użycie funkcji
array=[None]*100
for i in range(100):
    array[i]=int(random.random()*10*100)/100
sentinel_list_head = array_to_sentinel_list(array)
display_list_with_sentinel(sentinel_list_head)
print("\n======")
Sort(sentinel_list_head)
display_list_with_sentinel(sentinel_list_head)


    
        

    
