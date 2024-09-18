def merge(tab,L,M,P):
    left=tab[L:M+1]
    right=tab[M+1:P+1]
    leftIndex=0
    rightIndex=0
    tabIndex=L
    while leftIndex <= M -L and rightIndex <= P - M - 1 :
        if left[leftIndex]<=right[rightIndex]:
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


    
tab=[11,22,-33,22,1,0,-100,80,1,9]
mergeSort(tab,0,9)
print(tab)