class Tree:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def insertion(root,value):
    if root.data==value:
        return 
    if value<root.data:
        if root.left:
            insertion(root.left,value)
        else:
            root.left=Tree(value)
    else:
        if root.right:
            insertion(root.right,value)
        else:
            root.right=Tree(value)
def traversal(root):
    if root is None:
        return
    else:
        traversal(root.left)
        print(root.data,end=" ")
        traversal(root.right)
def search(root,val):
    if root.data==val:
        return True
    if val<root.data:
        if root.left:
            return search(root.left,val)
        else:
            return False
    else:
        if root.right:
            return search(root.right,val)
        else:
            return False
def minimum(root):
    if root.left is None:
        return root.data
    return minimum(root.left)
def maximum(root):
    if root.right is None:
        return root.data
    return maximum(root.right)
def deletion(root,key):
    if root is None:
        return root
    if key < root.data:
        root.left = deletion(root.left,key)
        return root
    if key > root.data:
        root.right = deletion(root.right,key)
        return root
    #we reach here when root is the node to be deleted
    #if root node is a leaf node
    if root.left is None and root.right is None:
        return None

    # if one of children is empty
    if root.left is None:
        temp = root.right
        root = None
        return temp
    elif root.right is None:
        temp = root.left
        root = None
        return temp
    
    #if both children exist
    
    succParent = root
    succ = root.right
    while succ.left!=None:
        succParent = succ
        succ = suuc.left
    
    #delete successor.since successor is always leftchild of parent we can safely make successors right
    #right child as left of its parent. if there is no succ,then assign succ ->right to succParent ->
    if succParent!=root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    root.data = succ.data
    return root

#driver code
elements=[17,4,1,20,9,23,18,34,18,4]
root=Tree(17)
elements.pop(0)
for i in elements:
    insertion(root,i)
traversal(root)
print()
ele=int(input("enter the element for search: "))
if search(root,ele):
    print("yes the value exits {}:".format(ele))
else:
    print("the value doestnot exists: ")
ans=minimum(root)
print("the smallest value in the tree: {}".format(ans))
print("the largest value in the Tree is: {}".format(maximum(root)))
deletion(root,1)
print("After deleting a node: ")
traversal(root)
print()
insertion(root,1)
traversal(root)
print()