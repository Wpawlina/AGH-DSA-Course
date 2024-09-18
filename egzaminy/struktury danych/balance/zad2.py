from zad2testy import runtests

class Node:
    def __init__(self):  # stwórz węzeł drzewa
        self.edges = []  # lista węzłów do których są krawędzie
        self.weights = []  # lista wag krawędzi
        self.ids = []  # lista identyfikatorów krawędzi
        self.sums = 0

    def addEdge(self, x, w, id):  # dodaj krawędź z tego węzła do węzła x
        self.edges.append(x)  # o wadze w i identyfikatorze id
        self.weights.append(w)
        self.ids.append(id)
    

def sumE(node):
     if node is not None:
            suma=0
            for i in range(len(node.edges)):
                suma+=node.weights[i]+sumE(node.edges[i])
            node.sums=suma
            return suma

def balance( T ):
    rootSum=sumE(T)
    res=-1
    minV=float('inf')
    def find(node):
        nonlocal res,minV
        if node is not None:
            for i in range(len(node.edges)):
                dif=abs((rootSum-node.weights[i]-node.edges[i].sums)-node.edges[i].sums)
                if dif<minV:
                    minV=dif
                    res=node.ids[i]
                find(node.edges[i])
    find(T)
    return res
    







   

    
runtests( balance )


