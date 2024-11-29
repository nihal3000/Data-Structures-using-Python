class Dequeue:
    def __init__(self):
        self.q = []

    def isEmpty(self, q):
        return len(q) == 0
    
    def insert_last(self, elem):
        if self.isEmpty(self.q):
            self.q.append(elem)
        else:
            self.q.append(elem)

    def delete_first(self):
        if self.isEmpty(self.q):
            print("The list is empty!!!")
        else:
            return self.q.pop(0)
        
    def insert_first(self,elem):
        self.q.insert(0,elem)

    def delete_last(self):
        if self.isEmpty(self.q):
            print("The list is empty!!!")
        else:
            return self.q.pop()
        
    def front(self):
        return self.q[0]
    
    def rear(self):
        return self.q[-1]
    
ql = Dequeue()

ql.insert_first(50)
ql.insert_first(60)
ql.insert_first(70)

print(ql.q)
print("\n")


del1 = ql.delete_last()
print(f"The rear element deleted is: {del1}")

ql.insert_last(80)
ql.insert_last(90)

print(ql.q)
print("\n")

del2 = ql.delete_first()
print(f"The front element deleted is: {del2}")

print(ql.q)
print("\n")

print(f"Front element in the queue: {ql.front()}")
print(f"Rear element of the queue is: {ql.rear()}")