from egzP5atesty import runtests 

def inwestor2 ( T ):
    n=len(T)
    res=0
    for i in range(n):
        j=i
        k=i
        while k<n and T[k]>=T[i]:
            k+=1
        k-=1
        while j>=0 and T[j]>=T[i]:
            j-=1
        j+=1
        res=max(res,(k-j+1)*T[i])
    return res

def inwestor ( T ):
    n=len(T)
    stack=[-1,0]
    L=[-1 for _ in range(n)]
    R=[n for _ in range(n)]
    for i in range(1,n):
        while stack[-1]!=-1 and T[stack[-1]]>=T[i]:
            R[stack[-1]]=i
            stack.pop()
        L[i]=stack[-1]
        stack.append(i)
    res=0
    for i in range(n):
        res=max(res,(R[i]-L[i]-1)*T[i])
    return res

        


runtests ( inwestor, all_tests=True )