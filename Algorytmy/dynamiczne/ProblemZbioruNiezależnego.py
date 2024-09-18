class Node:
    def __init__(self,weight):
        self.children=[]
        self.weight=weight
        self.f=-1
        self.g=-1
        self.fList=[]
        self.gList=[]

def pzn(root):
    def f(v):
        if v.f>=0: return v.f
        x=g(v)
        list=[]
        list.append(v)
        y=v.weight
        for u in v.children:
            y+=g(u)
            list.extend(u.gList)
        if y>=x:
            v.f=y
            v.fList=list
        else:
            v.f=x
            v.fList=v.gList
        return v.f

    def g(v):
        if v.g>=0: return v.g  
        v.g=0
        for u in v.children:
            v.g+=f(u)
            v.gList.extend(u.fList)
        return v.g
    f(root)

root=Node(50)
m1=Node(25)
m2=Node(10)
m3=Node(20)
root.children.append(m1)
root.children.append(m2)
root.children.append(m3)
ml1=Node(10)
ml2=Node(30)
m1.children.append(ml1)
m1.children.append(ml2)
ml3=Node(8)
m2.children.append(ml3)
ml4=Node(18)
ml5=Node(1)
ml6=Node(35)
m3.children.append(ml4)
m3.children.append(ml5)
m3.children.append(ml6)
e1=Node(1)
e2=Node(4)
e3=Node(10)
ml2.children.append(e1)
ml2.children.append(e2)
ml2.children.append(e3)
e4=Node(1)
e5=Node(1)
e6=Node(1)
ml5.children.append(e4)
ml5.children.append(e5)
ml5.children.append(e6)
i1=Node(15)
e3.children.append(i1)
i2=Node(1)
i3=Node(10)
e6.children.append(i2)
e6.children.append(i3)

pzn(root)
print(root.f)
for v in root.fList:
    print(v.weight)
    