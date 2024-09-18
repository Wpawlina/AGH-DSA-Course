from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def wideentall( T ):
   
    maxcnt=-1
    def height(node,cnt):
      nonlocal maxcnt
      if cnt>maxcnt:
        maxcnt=cnt
      if node.left is not None:
        height(node.left,cnt+1)
      if node.right is not None:
        height(node.right,cnt+1)
    height(T,1)
    L=[ 0 for _ in range(maxcnt)]
    def levels(node,level):
      nonlocal L
      L[level]+=1
      if node.left is not None:
        levels(node.left,level+1)
      if node.right is not None:
        levels(node.right,level+1)
    levels(T,0)
    n=len(L)
    maxv=-1
    maxi=-1
    for i in range(n-1,-1,-1):
        if L[i]>maxv:
          maxv=L[i]
          maxi=i
    res=0
    nodes=[]
    T.x=None
    def asignParent(node):
      if node.left is not None:
        node.left.x=node
        asignParent(node.left)
      if node.right is not None:
        node.right.x=node
        asignParent(node.right)
       
    asignParent(T)
    def findLevel(node,level):
      nonlocal maxi,nodes
      if node is None:
        return
      if level==maxi:
        nodes.append(node)
      if node.left is not None:
        findLevel(node.left,level+1)
      if node.right is not None:
        findLevel(node.right,level+1)
    findLevel(T,0)
    for node in nodes:
      while node is not None:
        temp=node.x
        node.x=None
        node=temp
    res=0
    def countToRemove(node):
      nonlocal res
      if node.x is not None:
        res+=1
      else:
        if node.left is not None:
          countToRemove(node.left)
        if node.right is not None:
          countToRemove(node.right)
    countToRemove(T)
    return res

    


    


    


      

    

        
       

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )