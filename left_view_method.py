class Tree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def leftview_helper(root):
    max_level_visited=[0]
    print_leftview(root,max_level_visited,1)
def print_leftview(node,max_level_visited,curr_level):
    if node is None:
        return 
    if max_level_visited[0]<curr_level:
        print(node.key,end=" ")
        max_level_visited[0]=curr_level
        print(max_level_visited)
    print_leftview(node.left,max_level_visited,curr_level+1)
    print_leftview(node.right,max_level_visited,curr_level+1)
root=Tree(20)
root.left=Tree(70)
root.right=Tree(90)
root.right.left=Tree(30)
root.right.left.left=Tree(10)
root.right.right=Tree(70)
leftview_helper(root)
print()
