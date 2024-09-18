from zad1testy import runtests

def merge(tab,L,M,P):
    left=tab[L:M+1]
    right=tab[M+1:P+1]
    leftIndex=0
    rightIndex=0
    tabIndex=L
    while leftIndex <= M -L and rightIndex <= P - M - 1 :
        if left[leftIndex][0]<=right[rightIndex][0]:
            tab[tabIndex]=left[leftIndex]
            leftIndex+=1
        else:
            tab[tabIndex]=right[rightIndex]
            rightIndex+=1
        tabIndex+=1
    while leftIndex <= M -L:
        tab[tabIndex]=left[leftIndex]
        leftIndex+=1
        tabIndex+=1
    while rightIndex <= P - M - 1:
        tab[tabIndex]=right[rightIndex]
        rightIndex+=1
        tabIndex+=1
def mergeSort(tab,L,P):
    if L==P:
        return
    M=(L+P)//2
    mergeSort(tab,L,M)
    mergeSort(tab,M+1,P)
    merge(tab,L,M,P)



def chaos_index( T ):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    mergeSort(T,0,n-1)
    k = 0
    for i in range(n):
        k = max(k, abs(T[i][1] - i))
    return k


runtests( chaos_index )
