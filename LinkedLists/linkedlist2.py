from Node import Node

class LinkedList2:
    def __init__(self):
        self.l = None

    def InsertFirst(self, elem):
        if(self.l is None):
            self.l = Node(elem)
        else:
            t = Node(elem)
            t.next = self.l
            self.l = t
    
    def DeleteFirst(self):
        if self.l is None:
            print("List is empty")
        else:
            t = self.l.val
            k = self.l
            self.l = self.l.next
            del k
            return t
    
    def InsertLast(self, elem):
        if self.l is None:
            self.l = Node(elem)
        else:
            t = Node(elem)
            k = self.l
            while k.next!=None:
                k = k.next
            k.next = t
            k = t

    def DeleteLast(self):
        
        k = self.l.next
        p = self.l
        while k.next!=None:
            k = k.next
            p = p.next
        
        t = k.val
        del k
        p.next = None
        return t

ll = LinkedList2()
ll.InsertFirst(50)
ll.InsertFirst(60)
ll.InsertFirst(70)
ll.InsertLast(20)
ll.InsertLast(30)
ll.InsertLast(80)

curr = ll.l

print("The list:")
while(curr!=None):
    print(curr.val, end=" ")
    curr = curr.next

del1 = ll.DeleteFirst()
print(f"Deleted element: {del1}")

del2 = ll.DeleteLast()
print(f"The last element deleted is {del2}")

curr = ll.l

while(curr!=None):
    print(curr.val, end=" ")
    curr = curr.next

