from Node import Node

class LinkedList:
    def __init__(self):
        self.l = None

    def InsertFirst(self, val):
        if self.l is None:
            self.l = Node(val)

        else:
            t = Node(val)
            t.next = self.l
            self.l = t

    # def delete_middle()

    def deleteFirst(self):
        if self.l is None:
            print("The list is empty, cannot delete anything!")
        else:
            t = self.l.val
            k = self.l
            self.l = self.l.next
            del k

    def insertLast(self, val):
        if self.l is None:
            self.l = Node(val)
        else:
            c = self.l

            while(c.next!=None):
                c= c.next
            t = Node(val)
            c.next = t

    def delete_middle(self, elem):
        if self.l is None:
            print("Error")
        else:
            
            t = self.l
            while t!=None and t.next!=None:
                if t.next.val==elem:
                   temp = t.next
                   t.next = t.next.next
                   del temp
                   print(f"Deleted node with value {elem}.")
                t = t.next


                
                
                    


li = LinkedList()
li.InsertFirst(5)
li.InsertFirst(10)
li.InsertFirst(15)
li.InsertFirst(20)

li.deleteFirst()
li.delete_middle(10)

li.insertLast(25)
li.insertLast(30)
curr = li.l

while curr!=None:
    print(curr.val, end=" ")
    curr = curr.next

