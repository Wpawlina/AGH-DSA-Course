# nieoptymalny

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def splitLinkedList(L):
    slow=L
    fast=L
    while fast.next is not None and fast.next.next is not None:
        fast=fast.next.next
        slow=slow.next
    right=Node(None)
    right.next=slow.next
    slow.next=None
    return L,right

def mergeLinkedList(left,right):
    result=left
    temp=Node(None)
    temp.next=left.next
    left=temp
    while left.next is not None and right.next is not None:
        if left.next.val<=right.next.val:
            result.next=left.next
            left.next=left.next.next
            result=result.next
        else:
            result.next=right.next
            right.next=right.next.next
            result=result.next
    if left.next is not None:
        result.next=left.next
    if right.next is not None:
        result.next=right.next
        
def mergeSort(L):
    if L.next  is not None and L.next.next is not None:
        left,right=splitLinkedList(L)
        mergeSort(left)
        mergeSort(right)
        mergeLinkedList(left,right)

def printLinkList(L):
    while L.next is not None:
        print(L.next.val,end='->')
        L=L.next

linked_list = Node(None)
linked_list.next = Node(5)
linked_list.next.next = Node(17)
linked_list.next.next.next = Node(8)
linked_list.next.next.next.next = Node(1)
linked_list.next.next.next.next.next = Node(3)
linked_list.next.next.next.next.next.next = Node(22)
printLinkList(linked_list)
print("\n--------")
mergeSort(linked_list)
printLinkList(linked_list)



