class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
max_dim=0
def height(root):
    if root is None:
        return 0
    lc_height=height(root.left)
    rc_height=height(root.right)

    global max_dim
    max_dim=max(max_dim,1+lc_height+rc_height)

    return 1 + max(lc_height,rc_height)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.left.left.right = Node(7)
root.left.right.right = Node(8)
root.left.left.left.left = Node(9)
root.left.right.right.right = Node(10)
print("the height of the root node is: {}".format(height(root)))
print("the diameter of the binary tree is: {}".format(max_dim,0))

