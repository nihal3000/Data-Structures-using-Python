from Node import Node

class Bst2:
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
                    c= c.rs
            if elem < p.val:
                p.ls = Node(elem)
            else:
                p.rs = Node(elem)
    
def searchBst(r, key):
    c = r
    while c!=None:
        if(key == c.val):
            return c.val
        elif key < c.val:
            c = c.ls
        else:
            c = c.rs
    return None

b = Bst2()
b.constbst(50)
b.constbst(23)
b.constbst(40)
b.constbst(20)
b.constbst(10)

print(searchBst(b.root, 40))

