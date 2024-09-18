from zad2testy import runtests

def partition(T,L,P):
    pivot=T[P]
    i=L-1
    for j in range(L,P):
        if T[j]>=pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[P]=T[P],T[i+1]
    return i+1

def quickSelect(T,L,P,k):
    if L<=P:
        pivotIndex=partition(T,L,P)
        if pivotIndex==k:
            return T[pivotIndex]
        elif pivotIndex<k:
            return quickSelect(T,pivotIndex+1,P,k)
        else:
            return quickSelect(T,L,pivotIndex-1,k)

def ksum(T, k, p):
    n=len(T)
    result=0
    for i in range(n-p+1):
        maxK=quickSelect(T[i:i+p],0,p-1,k-1)
        result+=maxK
    return result




   


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
T = [4, 2, 7, 1, 9, 3, 5]
#print(quickSelect(T[:3],0,2,1))