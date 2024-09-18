from kol2testy import runtests
from queue import Queue


def EdgeListToNlistNDW(E):
    n=len(E)
    m=max(E,key=lambda x:x[1])
    m=m[1]
    m=m+1
    G=[[]for _ in range(m)]
    for e in E:
        G[e[0]].append([e[1],e[2]])
        G[e[1]].append([e[0],e[2]])
    return G


def bfs(G,s):
    n=len(G)
    dist=[[float('inf') for _ in range(17)] for _ in range(n)]
    Q=Queue()
    value=16
    dist[s][value]=0