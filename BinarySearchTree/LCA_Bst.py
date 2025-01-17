from Node import Node
# from Bst import b

def Lca(root, n1, n2):
    # base case
    if root is None:
        return None
    # If both n1 and n2 are smaller than root, LCA must be in the left subtree
    if (n1<root.val and n2<root.val):
        return Lca(root.ls, n1, n2)
    
    # If both n1 and n2 are greater than root, LCA must be in the right subtree
    if (n1>root.val and n2>root.val):
        return Lca(root.rs, n1, n2)
    
    return root.val

root = Node(20)
root.ls = Node(8)
root.rs = Node(22)
root.ls.ls = Node(4)
root.ls.rs = Node(12)
root.ls.rs.ls = Node(10)
root.ls.rs.rs = Node(14)

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
print(Lca(root, n1, n2))
