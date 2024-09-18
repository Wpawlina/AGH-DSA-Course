from queue import PriorityQueue


class Letter:
    def __init__(self,letter,f):
        self.letter=letter
        self.f=f
        self.d=None
        self.parent=None
        self.left=None
        self.right=None
        self.code=None


def HuffmanCode(L):
    n=len(L)
    Q=PriorityQueue()
    for l in L:
        Q.put((l.f,l))
    root=None
    while True:
        l1=Q.get()[1]
        l2=Q.get()[1]
        l3=Letter(l1.letter+l2.letter,l1.f+l2.f)
        l1.parent=l3
        l2.parent=l3
        l3.left=l1
        l3.right=l2
        if Q.empty():
            root=l3
            break
        Q.put((l3.f,l3))
    def AsignCode(node,depth,code):
        if len(node.letter)==1:
            node.code=code
        node.d=depth
        if node.left is not None:
            AsignCode(node.left,depth+1,code+'0')
        if node.right is not None:
            AsignCode(node.right,depth+1,code+'1')
    AsignCode(root,0,'')
    CodedLength=0
    res=[]
    for letter in L:
        CodedLength+=letter.f*letter.d
        res.append((letter.letter,letter.code))
    return res,CodedLength


a=Letter('a',700)
b=Letter('b',200)
c=Letter('c',120)
d=Letter('d',300)
e=Letter('e',10)
L=[]
L.append(a)
L.append(b)
L.append(c)
L.append(d)
L.append(e)
print(HuffmanCode(L))



    
        
    


        











        