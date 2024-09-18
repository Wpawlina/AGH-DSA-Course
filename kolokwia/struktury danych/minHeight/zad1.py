from zad1testy import runtests
def inorder_traversal(root, nodes):
    if root:
        inorder_traversal(root.left, nodes)
        nodes.append(root)
        inorder_traversal(root.right, nodes)

def TreeAppend(root,node):
    node.parent=None
    node.left=None
    node.right=None
    while True:
        if node.value>root.value:
            if root.right is None:
                root.right=node
                node.parent=root
                return
            else:
                root=root.right
        else:
            if root.left is None:
                root.left=node
                node.parent=root
                return
            else:
                root=root.left


def preorder_traversal_print(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal_print(root.left)
        preorder_traversal_print(root.right)





def ConvertTree(p):
    res=None
    nodes=[]
    inorder_traversal(p,nodes)
    def median(T,l,p,cnt):
        nonlocal res
        if l>p:
            return
        i=l
        j=p
        while i<j:
            i+=1
            j-=1
       
        if cnt==1:
            
            res=T[j]
            res.parent=None
            res.left=None
            res.right=None
            
        else:
            TreeAppend(res,T[j])
        if i==j:
            if j-1>=l:
                median(T,l,j-1,cnt+1)
            if i+1<=p:
                median(T,i+1,p,cnt+1)
        else:
            if j-1>=l:
                median(T,l,j-1,cnt+1)
            if i<=p:
                median(T,i,p,cnt+1)
    median(nodes,0,len(nodes)-1,1)
    preorder_traversal_print(res)
    return res
    
   


runtests( ConvertTree )