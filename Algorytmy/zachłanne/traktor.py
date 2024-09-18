def traktorA(L,S,B):
    i=0
    res=0
    while i<B:
        for j in range(i+L,i,-1):
            if j>=B:
                return res
            if S[j]==True:
                res+=1
                i=j
                break
    return res
        
def traktorB(L,S,B):
    res=0
    pos=0
    stations=[]
    tank=L
    while True:
        cheapest=float('inf')
        next=-1
        for i in range(pos+1,pos+L+1):
            if i>B:
                break
            if S[pos]>S[i]:
                next=i
                break       
        if next==-1:
            if pos+L>=B:
                if B-pos>tank:
                    res+=(B-pos-tank)*S[pos]
                    stations.append((pos,B-pos-tank,(B-pos-tank)*S[pos]))
                    break
            for i in range(pos+1,pos+L+1):
                if cheapest>S[i]:
                    next=i
                    cheapest=S[i]
            stations.append((pos,L-tank,(L-tank)*S[pos]))
            res+=(L-tank)*S[pos]
            tank=L
        else:
            if next-pos>tank:
                res+=(next-pos-tank)*S[pos]
                stations.append((pos,next-pos-tank,(next-pos-tank)*S[pos]))
                tank+=(next-pos-tank) 
        tank=tank-(next-pos)
        pos=next
    return res,stations

L=8
B=[float('inf')]*33
B[2]=3
B[4]=8
B[7]=6
B[9]=11
B[10]=8
B[13]=4
B[18]=9
B[20]=13
B[22]=9
B[24]=7
B[29]=1
print(traktorB(L,B,32))
        

        
        






        

  



