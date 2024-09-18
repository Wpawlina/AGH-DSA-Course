def SortH(p,k):
    L=Node()
    L.next=p
    H=Node()
    new=H
    while L.next is not None:
        min=L
        i=0
        q=L
        while q.next is not None and i<k:
            if q.next.val<min.next.val:
                min=q
        if min.next.val<L.next.val:
            H.next=min.next
            H=H.next
            min.next,L.next,L.next.next=L.next,L.next.next,min.next.next
        else:
            H.next=L.next
            H=H.next
            L.next=L.next.next
    return new.next


