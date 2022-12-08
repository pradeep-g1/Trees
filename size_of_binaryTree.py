class Tree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def sizeof(root):
    if root is None:
        return 0
    else:
        return (1+sizeof(root.left)+sizeof(root.right))
root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.left.left=Tree(4)
root.left.right=Tree(5)
root.right.right=Tree(6)
print(sizeof(root))