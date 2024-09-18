from zad1testy import runtests


def intuse( I, x, y ):
    n = len( I )
    for i in range(n):
        I[i]=(I[i],i)
    I.sort(key=lambda x: x[0][0])
    start=[]
    end=[]
    for i in range(n):
        if I[i][0][0]==x:
            start.append(i)
        if I[i][0][1]==y:
            end.append(i)
    F=[False for _ in range(n)]
    P=[[] for _ in range(n)]
    for s in start:
        F[s]=True
    for i in range(n):
        if i in start:
            continue
        for j in range(i):
            if i!=j and F[j] and I[j][0][1]==I[i][0][0]:
                F[i]=True
                P[i].append(j)
    used=[False for _ in range(n)]
    stack=[]
    for e in end:
        if F[e]:
            stack.append(e)
    while len(stack)>0:
        i=stack.pop()
        used[i]=True
        for p in P[i]:
            if not used[p]:
                stack.append(p)
    res=[]
    for i in range(n):
        if used[i]:
            res.append(I[i][1])
    return res
        


            









  

   

    
runtests( intuse )


