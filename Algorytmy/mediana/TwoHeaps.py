def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapifyMax(T,n,i):
    maxIndex=i
    l=left(i)
    r=right(i)
    if l<n and T[l]>T[maxIndex]:
        maxIndex=l
    if r<n and T[r]>T[maxIndex]:
        maxIndex=r
    if maxIndex!=i:
        T[i],T[maxIndex]=T[maxIndex],T[i]
        heapifyMax(T,n,maxIndex)


def heapifyMin(T,n,i):
    minIndex=i
    l=left(i)
    r=right(i)
    if l<n and T[l]<T[minIndex]:
        minIndex=l
    if r<n and T[r]<T[minIndex]:
        minIndex=r
    if minIndex!=i:
        T[i],T[minIndex]=T[minIndex],T[i]
        heapifyMin(T,n,minIndex)

def heapMinPush(T,element):
    T.append(element)
    i=len(T)-1
    while parent(i)>=0:
        if T[parent(i)]<=T[i]:
            break
        T[i],T[parent(i)]=T[parent(i)],T[i]
        i=parent(i)

def heapMaxPush(T,element):
    T.append(element)
    i=len(T)-1
    while parent(i)>=0:
        if T[parent(i)]>=T[i]:
            break
        T[i],T[parent(i)]=T[parent(i)],T[i]
        i=parent(i)






def Median(T):
    highHeap=[]
    lowHeap=[]
    med=-float('inf')
    n=len(T)
    for i in range(n):
        #dodawanie elementu na odpowiedni stos
        if T[i]>=med:
            heapMinPush(highHeap,T[i])   
        else:
            lowHeap.append(T[i])
            heapifyMax(lowHeap,len(lowHeap),len(lowHeap)-1)
        
        #wyrownywanie stosów
        if len(highHeap)>len(lowHeap)+1:
            highHeap[0],highHeap[len(highHeap)-1]=highHeap[len(highHeap)-1],highHeap[0]
            temp=highHeap.pop()
            heapifyMin(highHeap,len(highHeap),0)
            heapMaxPush(lowHeap,temp)
        elif 1+len(highHeap)<len(lowHeap):
            lowHeap[0],lowHeap[len(lowHeap)-1]=lowHeap[len(lowHeap)-1],lowHeap[0]
            temp=lowHeap.pop()
            heapifyMax(lowHeap,len(lowHeap),0)
            heapMinPush(highHeap,temp)

    
        #ustalenie mediany
        if len(highHeap)>len(lowHeap):
            med=highHeap[0]
        else:
            med=lowHeap[0]
    return med

T=[24,-15,7,102,-56,33,0,91,-3,18,-77,42,5,-29,63,-8,11,-45,88,36,-12,72,-6,20,49,-91,2,13,-60,55]
print(Median(T))    
            


