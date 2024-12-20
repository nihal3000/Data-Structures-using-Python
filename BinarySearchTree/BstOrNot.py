from Node import Node
from Bst import Bst, b

def isBst(root, minval= float('-inf'), maxval= float('inf')):
    if root is None:
        return True
    if not minval < root.val < maxval:
        return False
    return (isBst(root.ls) and isBst(root.rs))

b.bstTraversal()
print(isBst(b.root))