from queue import Queue
from queue import PriorityQueue


def BFS(G,s,f):
    Q=Queue()
    n=len(G)
    visted={}
    for v in G.keys():
        visted[v]=False
    visted[s]=True
    Q.put(s)
    while not Q.empty():
        u=Q.get()
        for v in G[u]:
            if not visted[v[0]]:
                Q.put(v[0])
                visted[v[0]]=True
    return visted[f]


def Dijkstra(G,s,f):
    n=len(G)
    distance={}
    for v in G.keys():
        distance[v]=float('inf')
    distance[s]=0
 
    
    Q=PriorityQueue()
    distance[s]=0
    Q.put((distance[s],s))
    while not Q.empty():
        u=Q.get()
        for v in G[u[1]]:
            if distance[v[0]]> distance[u[1]]+v[1]:
                distance[v[0]]=distance[u[1]]+v[1]
                Q.put((distance[v[0]],v[0]))
    return distance[f]

def BFS2(G,s,k):
    Q=Queue()
    n=len(G)
    visted={}
    for v in G.keys():
        visted[v]=False
    visted[s]=True
    Q.put((s,0,0))
    m=0
    while not Q.empty():
        u,steps,dist=Q.get()
        m=max(m,dist)
        if steps==k:
            continue
        for v in G[u]:
            if not visted[v[0]]:
                Q.put((v[0],steps+1,dist+v[1]))
                visted[v[0]]=True
    return m
    

def connectingProblem(L,a,b,k):
    G={}
    G[a]=[]
    G[b]=[]
    for l in L:
        c,d,w=l
        G[c]=[]
        G[d]=[]
    for l in L:
        c,d,w=l
        G[c].append([d,w])
    res1=BFS(G,a,b)
    res2=-1
    if res1:
          res2=Dijkstra(G,a,b)
    res3=0
    for v in G.keys():
        res3=max(res3,BFS2(G,v,k))
    return res1,res2,res3

def test_connectingProblem():
    # Test Case 1: Simple connected intervals
    L1 = [(1, 2, 1), (2, 3, 2), (3, 4, 3)]
    a1, b1 = 1, 4
    k1 = 2
    expected_output1 = (True, 6, 5)  # Connectivity: True, Minimal cost: 6, Longest interval with at most 2 intervals: 3
    result1 = connectingProblem(L1, a1, b1, k1)
    assert result1 == expected_output1, f"Test Case 1 Failed: {result1}"

    # Test Case 2: Disconnected intervals
    L2 = [(1, 2, 1), (2, 3, 2), (4, 5, 1)]
    a2, b2 = 1, 5
    k2 = 2
    expected_output2 = (False, -1, 3)  # Connectivity: False, Minimal cost: -1 (not reachable), Longest interval with at most 2 intervals: 3
    result2 = connectingProblem(L2, a2, b2, k2)
    assert result2 == expected_output2, f"Test Case 2 Failed: {result2}"

    # Test Case 3: All intervals connected
    L3 = [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 5, 4)]
    a3, b3 = 1, 5
    k3 = 3
    expected_output3 = (True, 10, 9)  # Connectivity: True, Minimal cost: 10, Longest interval with at most 3 intervals: 4
    result3 = connectingProblem(L3, a3, b3, k3)
    assert result3 == expected_output3, f"Test Case 3 Failed: {result3}"

    # Test Case 4: Single interval
    L4 = [(1, 2, 1)]
    a4, b4 = 1, 2
    k4 = 1
    expected_output4 = (True, 1, 1)  # Connectivity: True, Minimal cost: 1, Longest interval with at most 1 interval: 1
    result4 = connectingProblem(L4, a4, b4, k4)
    assert result4 == expected_output4, f"Test Case 4 Failed: {result4}"

    # Test Case 5: No intervals
    L5 = []
    a5, b5 = 1, 2
    k5 = 1
    expected_output5 = (False, -1, 0)  # Connectivity: False, Minimal cost: -1 (not reachable), Longest interval with at most 1 interval: 0
    result5 = connectingProblem(L5, a5, b5, k5)
    assert result5 == expected_output5, f"Test Case 5 Failed: {result5}"

    # Test Case 6: Complex graph with multiple paths
    L6 = [(1, 2, 1), (2, 3, 2), (1, 3, 5), (3, 4, 1), (4, 5, 2)]
    a6, b6 = 1, 5
    k6 = 3
    expected_output6 = (True, 6, 8)  # Connectivity: True, Minimal cost: 6, Longest interval with at most 3 intervals: 4
    result6 = connectingProblem(L6, a6, b6, k6)
    assert result6 == expected_output6, f"Test Case 6 Failed: {result6}"

    # Test Case 7: Intervals with multiple weights
    L7 = [(1, 2, 1), (2, 3, 2), (3, 4, 1), (1, 3, 10)]
    a7, b7 = 1, 4
    k7 = 2
    expected_output7 = (True, 4, 11)  # Connectivity: True, Minimal cost: 4, Longest interval with at most 2 intervals: 3
    result7 = connectingProblem(L7, a7, b7, k7)
    assert result7 == expected_output7, f"Test Case 7 Failed: {result7}"

    # Test Case 8: k too small to connect a and b
    L8 = [(1, 2, 1), (2, 3, 1), (3, 4, 1)]
    a8, b8 = 1, 4
    k8 = 1
    expected_output8 = (True, 3, 1)  # Connectivity: True, Minimal cost: 3, Longest interval with at most 1 interval: 1
    result8 = connectingProblem(L8, a8, b8, k8)
    assert result8 == expected_output8, f"Test Case 8 Failed: {result8}"

    print("All test cases passed!")

test_connectingProblem()








