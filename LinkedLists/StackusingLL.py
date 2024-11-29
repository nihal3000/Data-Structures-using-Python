from Node import Node

class StackLL:
    def __init__(self):
        self.s = None
    
    def empty(self):
        if self.s is None:
            return True
        else:
            return False
    
    def Push(self, elem):
        if self.s is None:
            self.s = Node(elem)
        else:
            t = Node(elem)
            t.next = self.s
            self.s = t
    
    def Pop(self):
        if self.s is None:
            print("Stack is empty")
            return None
        else:
            t = self.s.val
            k = self.s
            self.s = self.s.next
            del k
            return t

    def size(self):
        k = self.s
        count = 0
        while(k!=None):
            k = k.next
            count = count + 1
        return count
    
    def Top(self):
        return self.s.val
    
stack = StackLL()


stack.Push(10)
stack.Push(20)
stack.Push(30)
stack.Push(40)
stack.Push(50)

print(f"Original size of stack is: {stack.size()}")

popElem = stack.Pop()
print("The Popped element is: ", popElem)

curr = stack.s

print(f"Size of stack after deletion: {stack.size()}")

while(curr!=None):
    print(curr.val, end=" ")
    curr = curr.next

print(f"The Top of the stack is: {stack.Top()}")

