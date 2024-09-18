from math import log10


def digits(n):
    return int(log10(n))+1

def countigSort(T,d):
    k=10
    n=len(T)
    count=[0]*k
    for num in T:
        count[(num//d)%10]+=1
    for i in range(1,n):
        count[i]+=count[i-1]
    result=[0]*n 
    for i in range(n-1,-1,-1):
        result[count[(T[i]//10)%10]-1]=T[i]
        count[(T[i]//10)%10]-=1
    return result


     




def radixSort(T):
    k=digits(max(T))
    for i in range(k):
        T=countigSort(T,10*i)

