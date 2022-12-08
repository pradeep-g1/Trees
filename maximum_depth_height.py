class Tree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def postordertraversal(root):
    if root:
        postordertraversal(root.left)
        postordertraversal(root.right)
        print(root.key,end=" ")
def maximumheight(root):
    if root is None:
        #if considering height from 1 change it to -1
        return 0
    else:
        lheight=maximumheight(root.left)
        rheight=maximumheight(root.right)
    if lheight>rheight:
        return lheight+1
    else:
        return rheight+1
root=Tree(10)
root.left=Tree(9)
root.right=Tree(11)
root.left.left=Tree(8)
root.left.right=Tree(7)
root.right.left=Tree(12)
root.left.left.left=Tree(5)
postordertraversal(root)
print("\nmaximum height of the Tree: ",maximumheight(root))