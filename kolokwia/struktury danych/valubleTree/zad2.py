from zad2testy import runtests

class Node:
    def __init__(self):
        self.left = None  # lewe podrzewo
        self.leftval = 0  # wartość krawędzi do lewego poddrzewa jeśli istnieje
        self.right = None  # prawe poddrzewo
        self.rightval = 0  # wartość krawędzi do prawego poddrzewa jeśli istnieje
        self.X = None  # miejsce na dodatkowe dane


def valuableTree(T, k):
    if k==0:
        return 0
    if k<0:
        return None
    cnt=-1
    def traverseTree(root):
        nonlocal cnt
        if root is None:
            return
        cnt+=1
        root.X=cnt
        traverseTree(root.left)
        traverseTree(root.right)
    traverseTree(T)
    F=[[-float('inf') for _ in range(k+1)] for _ in range(cnt+2)]
    
    for i in range(cnt+1):
        F[i][0]=0
    def f(node,k):
        
        if node is None:
            return None
        if k==0:
            F[node.X][k]=0
            return 0
        if F[node.X][k]!=-float('inf'):
            return F[node.X][k]
        
        if node.left is not None and node.right is not None:
            best=-float('inf')
            if k>=3:
                best=max(f(node.left,k-1)+node.leftval,f(node.right,k-1)+node.rightval,f(node.left,k-2)+node.leftval+node.rightval,f(node.right,k-2)+node.rightval+node.leftval)
            elif k==2:
                best=max(f(node.left,1)+node.leftval,f(node.right,1)+node.rightval,node.leftval+node.rightval)
            elif k==1:
                best=max(node.leftval,node.rightval)
            else:
                return 0
            for l in range(1,k-2):
                for r in range(1,k-2):
                    if l+r==k-2:
                        best=max(best,f(node.left,l)+f(node.right,r)+node.rightval+node.leftval)
            F[node.X][k]=best
            return best    
        if node.left is None and node.right is None:
            return 0
        if node.left is None:
            F[node.X][k]=f(node.right,k-1)+node.rightval
            return F[node.X][k]
        if node.right is None:
            F[node.X][k]=f(node.left,k-1)+node.leftval
            return F[node.X][k]
    def startRek(node):
        if node:
            f(node,k)
            startRek(node.left)
            startRek(node.right)
    startRek(T)
    res=-float('inf')
    for i in range(cnt+2):
        res=max(res,F[i][k])
    return res if res>-float('inf') else None
    


        
    
runtests(valuableTree)
