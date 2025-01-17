class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DequeDLL:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size==0
    
    def size(self):
        return self.size
    
    def addFirst(self, data):
        if self.isEmpty():
            self.front = self.rear = Node(data)

        else:
            new_node = Node(data)

            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def addLast(self, data):
        if self.isEmpty():
            self.front = self.rear = Node(data)
        else:
            new_node = Node(data)
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.size += 1


    def deleteFirst(self):
        if self.isEmpty():
            return None
        if self.front == self.rear:
            self.front = self.rear = None

        else:

            self.front = self.front.next
            self.front.prev = None
        self.size -= 1


    def deleteLast(self):
        if self.isEmpty():
            return None
        if self.front == self.rear:
            self.front = self.rear = None

        else:
            self.rear = self.rear.prev
            self.rear.next = None

        self.size -= 1

    def display(self):
        curr = self.front
        while(curr!=None):
            print(curr.data, end=" ")
            curr = curr.next
        print("None")

qll = DequeDLL()

qll.addFirst(20)
qll.addFirst(30)

qll.addLast(40)
qll.addLast(50)

qll.deleteFirst()
qll.deleteLast()

qll.display()
