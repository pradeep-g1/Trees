class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def get_lca(root,val1,val2):
    #base case and handles case 4
    if root is None:
        return None
    #case 1
    if root.data==val1 or root.data==val2:
        return root
    left_lca=get_lca(root.left,val1,val2)
    right_lca=get_lca(root.right,val1,val2)
    
    # case 2 If its left subtree, has one node & the right subtree the other, current node is LCA
    if left_lca and right_lca:
        return root

    # case 3
    # If its subtree has both the node then LCA will also be in the subtree, check for LCA
    # in below subtree
    return left_lca if left_lca is not None else right_lca


#driver code
root=Tree(70)
root.left=Tree(20)
root.right=Tree(30)
root.left.left=Tree(50)
root.left.left.left=Tree(60)
root.left.left.left.left=Tree(90)
root.left.right=Tree(10)
root.left.right.right=Tree(80)
root.left.right.right.right=Tree(100)
root.left.left.right=Tree(40)
root.left.left.right.right=Tree(110)
lca=get_lca(root,90,110)
print("the lowest common ancestor is {}".format(lca.data))
