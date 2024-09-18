from math import log2
def parent(i):
        return (i-1)//2
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2

class Tree:
    def __init__(self,T):
        n=len(T)
        m=0
        n2=int(log2(n))
        if log2(n)!=float(int(log2(n))):
            n2=int(log2(n))+1
        for i in range(0,n2+1):
            m+=pow(2,i)
        self.A=[0 for i in range(m)]
        self.m=m
        self.n=pow(2,n2)
        start=m-pow(2,n2)
        self.start=start
        for i in range(n):
            self.A[i+start]=T[i]
        end=m
        print(self.A)
        for j in range(n2,0,-1):
            print(start,end)
            for i in range(start+1,end,2):
                self.A[parent(i)]=self.A[i]+self.A[i-1]
            end=start
            start=start-pow(2,j-1)
        self.A[0]=self.A[left(0)]+self.A[right(0)]

    def printTree(self):
        print(self.A)
    
    def changeVal(self,i,value):
        i=i+self.start
        dif=value-self.A[i]
        while(i>=0):
            self.A[i]+=dif
            i=parent(i)
    def sumOfInt(self,i,j):
        l=0
        p=self.n-1
        res=0
        stack=[]
        stack.append((0,l,p,i,j))
        while len(stack)>0:
            root,l,p,i,j=stack.pop()
            if i==l and j==p:
                res+=self.A[root]
                continue
            m=(l+p)//2
            if i<=m:
                stack.append((left(root),l,m,i,min(j,m)))
            if j>m:
                stack.append((right(root),m+1,p,max(i,m+1),j))
        return res









    

T=[1,3,2,4,3,7,3,6]
tree=Tree(T)
tree.printTree()
print(tree.sumOfInt(1,5))










 


