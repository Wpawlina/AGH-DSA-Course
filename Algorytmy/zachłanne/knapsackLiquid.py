def knapsackLiqued(P,W,L):
    n=len(W)
    items=[(P[i],W[i]) for i in range(n)]
    items.sort(key=lambda x : x[0]/x[1],reverse=True)
    res=[]
    value=0
    for item in items:
        if L==0:
            break
        if L>=item[1]:
            value+=item[0]
            res.append((item[0],item[1]))
            L-=item[1]
        else:
            value+=item[0]*(L/item[1])
            res.append((item[0],L))
            L=0
            break
    return value,res

P=[2,1,1,1,1,1]
W=[5,1,1,1,1,1]
L=5
print(knapsackLiqued(P,W,L))