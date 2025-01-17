from Node import Node

class Bst:
    def __init__(self):
        self.root = None
        self.kth_largest = None
        self.count = 0

    def constbst(self, elem):
        if self.root is None:
            self.root = Node(elem)
        else:
            p = None
            c = self.root

            while(c!=None):
                p = c
                if elem<c.val:
                    c = c.ls
                else:
                    c = c.rs
                
            if elem<p.val:
                p.ls = Node(elem)
            else:
                p.rs = Node(elem)


    # def kth_largest_util(self, root, k):
    #     if root is None and self.count>=k:
    #         return
        
    #     # Tranverse right
    #     self.kth_largest_util(root.rs, k)

    #     self.count+=1

    #     if self.count==k:
    #         self.kth_largest = root.val
    #         return
    #     # Tranverse left
    #     self.kth_largest_util(root.ls, k)

    # def find_kth(self, k):
    #     self.count = 0
    #     self.kth_largest = None
    #     self.kth_largest_util(self.root, k)
    #     return self.kth_largest
    
    # def rev_inorder(node)

bst = Bst()

values = [15, 10, 20, 8, 12, 17, 25]
for value in values:
    bst.constbst(value)

print(bst.find_kth(bst.root, 4))