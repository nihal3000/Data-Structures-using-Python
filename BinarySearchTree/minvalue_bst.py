from Node import Node

def inorder(root, sorted_inorder):
    if root is None:
        return
    
    # left tranverse
    inorder(root.ls, sorted_inorder)

    sorted_inorder.append(root.val)

    # Right tranverse
    inorder(root.rs, sorted_inorder)

def minvalue(root):
    if root is None:
        return -1
    sorted_inorder = []
    inorder(root, sorted_inorder)
    return sorted_inorder[0] # First element contains the minvalue

if __name__ == "__main__":
    root = Node(5)
    root.ls = Node(4)
    root.rs = Node(6)
    root.ls.ls = Node(1)
    root.rs.rs = Node(7)
    root.ls.ls.ls = Node(1)
    
    print(minvalue(root))