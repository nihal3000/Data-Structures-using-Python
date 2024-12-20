from Node import Node

class Bst:
    def __init__(self):
        self.root = None

    def constbst(self, elem):
        if self.root is None:
            self.root = Node(elem)
        else:
            p = None
            c = self.root

            while c!=None:
                p = c
                if elem<c.val:
                    c = c.ls
                else:
                    c = c.rs
            if elem<p.val:
                p.ls = Node(elem)
            else:
                p.rs = Node(elem)

    def bstTraversal(self):
        def inorder(root):
            if root!=None:
                inorder(root.ls)
                print(root.val)
                inorder(root.rs)
        inorder(self.root)


b = Bst()
n = int(input("Enter size:"))
for i in range(n):
    elem = int(input("Enter element:"))
    b.constbst(elem)

b.bstTraversal()