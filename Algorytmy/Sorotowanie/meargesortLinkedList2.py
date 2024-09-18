class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge(L1,L2):
    result=head=Node(None)
    while L1 is not None and L2 is not None:
        if L1.val <= L2.val:
            result.next=L1
            L1=L1.next
            result=result.next
        else:
            result.next=L2
            L2=L2.next
            result=result.next
    if L1 is not None:
        result.next=L1
    if L2 is not None:
        result.next=L2
    return head.next
def end(L):
    while L.next is not None:
        L=L.next
    return L
def extractSeries(L):
    while L.next is not None and L.val<=L.next.val:
        L=L.next
    new=L.next
    L.next=None
    return new
def mergeSort(L):
    H=L
    L=L.next
    if L is None:
        return None
    endL=end(L)
    while True:
        L2=extractSeries(L)
        if L2 is None:
            H.next=L
            return 
        L3=extractSeries(L2)
        L=merge(L,L2)
        if L3 is None:
            H.next=L
            return None
        endL.next=L
        endL=end(L)
        L=L3


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
        







