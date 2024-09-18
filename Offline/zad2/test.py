from zad2testy import runtests

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2


def heapify(T,i):
    n=len(T)
    maxIndex=i
    l=left(i)
    p=right(i)
    if l<n and  T[maxIndex][0]<T[l][0]:
        maxIndex=l
    if p<n and T[maxIndex][0]<T[p][0]:
        maxIndex=p
    if maxIndex!=i:
        T[maxIndex],T[i]=T[i],T[maxIndex]
        heapify(T,maxIndex)
def buildHeap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T,i)
def extractFromHip(heap):
    n=len(heap)
    heap[0],heap[n-1]=heap[n-1],heap[0]
    result=heap.pop()
    heapify(heap,0)
    return result
def insertIntoHeap(heap,element):
    heap.append(element)
    n=len(heap)
    i=n-1
    while parent(i)>=0:
        if heap[parent(i)][0]>=heap[i][0]:
            return
        heap[parent(i)],heap[i]=heap[i],heap[parent(i)]
        i=parent(i)   





def ksum(T, k, p):
    n=len(T)
    pomT=[]
    sum=0
    for i in range(n):
        pomT.append((T[i],i))
    buildHeap(pomT)
    for i in range(n-p+1):
        temp=[]
        cnt=0
        while cnt<k:
            val,index=extractFromHip(pomT)
            #print(val,end=',')
            if i <= index <= i+p-1:
                cnt+=1
               
            if i < index:
                temp.append((val,index))
        #print('\n')
        sum+=val
        for j in range(len(temp)):
            insertIntoHeap(pomT,temp[j])
    return sum
        
        




    


    # tu prosze wpisac wlasna implementacje


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
#T = [4, 2, 7, 1, 9, 3, 5]
#print(ksum(T,2,3))



