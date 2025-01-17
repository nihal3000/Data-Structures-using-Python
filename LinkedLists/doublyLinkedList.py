class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            if new_node.prev is None:
                self.head = new_node
        return new_node

    # Insertion at the end
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
            curr = new_node
        return new_node

    # Insertion after a given node
    def insert_after_node(self, node, data):
        curr = self.head
        new_node = Node(data)
        new_node.prev = node
        new_node.next = node.next

        if node.next!=None:
            node.next.prev = new_node
        node.next = new_node

        return new_node
    
    # Deletion at the beginning
    def delete_at_beginning(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            self.head = None
            return self.head
        
        new_head = self.head.next
        self.head = new_head
        new_head.prev = None

        return new_head
    

    # Deletion at end
    def delete_at_end(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return self.head
        
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.prev.next = None
        curr = None

        return curr


    def display(self):
        if self.head is None:
            print("Empty!!")
            return
        else:
            curr = self.head
            while curr!=None:
                print(curr.data, end=' <-> ')
                curr = curr.next
            print("None")


dll = DoublyLinkedList()

node1 = dll.insert_at_beginning(5)
node2 = dll.insert_at_beginning(10)
node3 = dll.insert_at_beginning(15)
node4 = dll.insert_at_beginning(20)

node5 = dll.insert_at_end(25)
node6 = dll.insert_at_end(30)

node7 = dll.insert_after_node(node5, 27)

node8 = dll.insert_after_node(node7, 29)

del1 = dll.delete_at_beginning()
del2 = dll.delete_at_beginning()

del3 = dll.delete_at_end()
dll.display()


