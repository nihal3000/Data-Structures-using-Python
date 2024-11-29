from Node import Node

class Dequeue:
    def __init__(self):
        self.f = None
        self.r = None

    def insert_first(self, elem):
        t = Node(elem)
        if self.r is None:
            self.f = t
            self.r = t
        else:
            t.next = self.f
            self.f = t

    def insert_last(self, elem):
        t = Node(elem)
        if self.r is None:
            self.f = t
            self.r = t
        else:
            self.r.next = t
            self.r = t

    def delete_first(self):
        if self.r is None:
            print("Queue is empty!!!")
        else:
            t = self.f.val
            k = self.f
            self.f = self.f.next
            del k
    
    def delete_last(self):
        if self.r is None:
            print("Queue is empty")
        else:

            k = self.f
            while(k.next!=self.r):
                k = k.next
            t = self.r
            self.r = k
            self.r.next = None
            del t

deq = Dequeue()

deq.insert_last(50)
deq.insert_last(60)
deq.insert_last(70)

deq.delete_last()
deq.insert_first(21)
deq.insert_first(31)
deq.delete_first()
curr = deq.f

while(curr!=None):
    print(curr.val, end=" ")
    curr = curr.next