class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.span = None
        self.height = 0

def TreeAppend(root, value):
    if root.value > value:
        if root.left is None:
            new = Node(value)
            new.parent = root
            new.span = [root.span[0], root.value]
            root.left = new
        else:
            TreeAppend(root.left, value)
    else:
        if root.right is None:
            new = Node(value)
            new.parent = root
            new.span = [root.value, root.span[1]]
            root.right = new
        else:
            TreeAppend(root.right, value)

# Add leaf nodes with spans
def addLeafs(root):
    if root.left is None:
        new = Node('x')
        new.span = [root.span[0], root.value]
        new.parent = root
        root.left = new
    else:
        addLeafs(root.left)
    if root.right is None:
        new = Node('x')
        new.span = [root.value, root.span[1]]
        new.parent = root
        root.right = new
    else:
        addLeafs(root.right)

def checkInt(root, curInt, orgInt):

    if curInt[0] < root.value:
        checkInt(root.left, [curInt[0], min(root.value, curInt[1])], orgInt)
    if curInt[1] > root.value:
        checkInt(root.right, [max(curInt[0], root.value), curInt[1]], orgInt)

def initTree(intervals):
    points = set()
    for interval in intervals:
        points.add(interval[0])
        points.add(interval[1])
    points = list(points)
    points.sort()
    n = len(points)
    L = 0
    P = n - 1
    m = (L + P) // 2
    root = Node(points[m])
    root.span = [-float('inf'), float('inf')]
    stack = []
    stack.append((L, m - 1))
    stack.append((m + 1, P))
    while len(stack) > 0:
        l, p = stack.pop()
        if l <= p:
            m = (l + p) // 2
            TreeAppend(root, points[m])
            stack.append((l, m - 1))
            stack.append((m + 1, p))
    addLeafs(root)
    def checkInt(root, curInt, orgInt):
        mh=root.height
        if root.left is None and root.right is None:
            return mh
        if curInt[0] < root.value:
           mh=max(mh,checkInt(root.left, [curInt[0], min(root.value, curInt[1])], orgInt))
        if curInt[1] > root.value:
           mh=max(mh,checkInt(root.right, [max(curInt[0], root.value), curInt[1]], orgInt))
        return mh
    def addInt(root, curInt, orgInt,height):
        if root.span == curInt:
            root.height=max(height,root.height)
            return 
        if curInt[0] < root.value:
            addInt(root.left, [curInt[0], min(root.value, curInt[1])], orgInt,height)
        if curInt[1] > root.value:
            addInt(root.right, [max(curInt[0], root.value), curInt[1]], orgInt,height)


    for interval in intervals:
        interval_copy = list(interval)
        mh=checkInt(root, interval_copy, interval)
        addInt(root,interval_copy,interval,mh+1)
    return root

def cntInts(root):
    mh=0
    def traverseTree(root):
        nonlocal mh
        mh=max(mh,root.height)
        if root.left is not None:
            traverseTree(root.left)
        if root.right is not None:
            traverseTree(root.right)
    traverseTree(root)
    return mh

intervals = [(1,3),(5,7),(10,11),(2,6),(4,8),(-1,5)]
root = initTree(intervals)
print(cntInts(root))

