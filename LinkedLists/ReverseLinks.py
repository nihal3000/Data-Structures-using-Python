from Node import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, elem):
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next!=None:
                curr = curr.next
            curr.next = new_node
    
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        curr = self.head
        while curr!=None:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

    def reverse(self):
        prev = None
        curr = self.head
        while curr!=None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

s = SinglyLinkedList()

s.append(10)
s.append(20)
s.append(30)
s.append(40)

print("Original list:")
s.display()

s.reverse()
print("reverse list:")
s.display()