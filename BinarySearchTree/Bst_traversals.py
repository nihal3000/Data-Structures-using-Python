from Node import Node

class Bst:
    def __init__(self):
        self.root = None

    def constbst(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            p = None
            c = self.root

            while c!=None:
                p = c
                if val < c.val:
                    c = c.ls
                else:
                    c = c.rs
            if val < p.val:
                p.ls = Node(val)
            else:
                p.rs = Node(val)

    def preorder_traversal(self):
        def preorder(root):
            if root!=None:
                print(root.val, end=" ")
                preorder(root.ls)
                preorder(root.rs)
        preorder(self.root)
        print()

    def inorder_traversal(self):
        def inorder(root):
            if root!=None:
                inorder(root.ls)
                print(root.val, end=" ")
                inorder(root.rs)
        inorder(self.root)
        print()

    def postorder_traversal(self):
        def postorder(root):
            if root!=None:
                postorder(root.ls)
                postorder(root.rs)
                print(root.val, end=" ")
        postorder(self.root)


bst = Bst()

bst.constbst(10)
bst.constbst(20)
bst.constbst(5)
bst.constbst(12)
bst.constbst(45)
bst.constbst(34)

print("Preorder traversal")
bst.preorder_traversal()

print("Inorder traversal")
bst.inorder_traversal()

print("Postorder traversal")
bst.postorder_traversal()
