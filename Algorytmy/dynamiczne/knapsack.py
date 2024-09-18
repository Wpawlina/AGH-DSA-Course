def  knapsack(W,P,B):
    n=len(W)
    F=[[0 for _ in range(B+1)] for _ in range(n)]
    for b in range(W[0],B+1):
        F[0][b]=P[0]
    for b in range(B+1):
        for i in range(1,n):
            F[i][b]=F[i-1][b]
            if b-W[i]>=0:
                F[i][b]=max(F[i][b],F[i-1][b-W[i]]+P[i])
    return F[n-1][B],F

def items(F,W,P,B):
    res=[]
    n=len(W)
    i=n-1
    b=B
    while i>0:
        if b>=W[i] and F[i-1][b-W[i]]+P[i]>F[i-1][b]:
            res.append(i)
            b-=W[i]
        i-=1
    if b>=W[0]:
        res.append(0)
    res=res[::-1]
    return res

W = [3, 5, 2, 6, 7, 9]
P = [30, 50, 25, 60, 70, 80]
B = 15


max_value, F = knapsack(W, P, B)
included_items = items(F, W,P, B)

print("Maximum value:", max_value)
print("Items included:", included_items)