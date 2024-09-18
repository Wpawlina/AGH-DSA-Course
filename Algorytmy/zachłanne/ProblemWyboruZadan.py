def overlapping(L,i):
    n=len(L)
    res=[]
    for j in range(n):
        if i!=j:
            if not (L[i][1] <= L[j][0] or L[i][0] >= L[j][1]):
                res.append(j)
    return res


def PWZ(LZ):
    L=LZ.copy()
    L.sort(key=lambda x:x[1])
    n=len(L)
    overlap=[False for _ in range(n)]
    res=[]
    for i in range(n):
        if not overlap[i]:
            res.append(i)
            curOverLap=overlapping(L,i)
            for j in curOverLap:
                overlap[j]=True
    return res

LZ = [(1, 10),(1,8),(2,6),(3,4),(11,20),(15,22),(21,30),(31,40),(33,39),(35,38),(36,37)]


wybrane_przedzialy = PWZ(LZ)
print("Wybrane przedziały:",[LZ[i] for i in wybrane_przedzialy])
print("Indeksy wybranych przedziałów:",  wybrane_przedzialy)    