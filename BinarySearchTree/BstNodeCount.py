from Bst import Bst, b

def getCount(root, l, h):
    if root is None:
        return 0
    if root.val >=l and root.val<=h:
        return 1 + getCount(root.ls, l, h) + getCount(root.rs, l ,h)
    elif root.val<l:
        return getCount(root.rs, l, h)
    else:
        return getCount(root.ls, l, h)
    
b.bstTraversal()
print("count: ", getCount(b.root, 5, 15))