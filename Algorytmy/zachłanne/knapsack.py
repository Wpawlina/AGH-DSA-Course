def knapsack(P,W,L):
    initL=L
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
    res2=[]
    value2=0
    L=initL
    items.sort(key=lambda x: x[0],reverse=True)
    for item in items:
        if L==0:
            break
        if L>=item[1]:
            value2+=item[0]
            res2.append((item[0],item[1]))
            L-=item[1]
    if value>value2:
        return value,res
    else:
        return value2,res2
    


W = [3, 5, 2, 6, 7, 9]
P = [30, 50, 25, 60, 70, 80]
B = 15


max_value, included_items = knapsack(P, W, B)
 

print("Maximum value:", max_value)
print("Items included:", included_items)
