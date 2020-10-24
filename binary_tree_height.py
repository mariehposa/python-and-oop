class Node:
    def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 

    # this is a node of the tree , which contains info as data, left , right
def height(root):
    if root is None:
        return -1
    else:
        right_subtree = height(root.right)
        left_subtree = height(root.left)

        return (max(right_subtree, left_subtree)) + 1