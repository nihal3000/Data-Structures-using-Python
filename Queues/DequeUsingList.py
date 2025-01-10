class Deque:
    def __init__(self):
        self.items = []
    
    # Check if deque is empty
    def is_empty(self):
        return len(self.items) == 0
    
    # Add element to the front of the deque
    def add_front(self, item):
        self.items.insert(0, item)
    
    # Add element to the rear of the deque
    def add_rear(self, item):
        self.items.append(item)
    
    # Remove element from the front of the deque
    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    
    # Remove element from the rear of the deque
    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    # Get the element at the front of the deque
    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    
    # Get the element at the rear of the deque
    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    # Return the number of elements in the deque
    def size(self):
        return len(self.items)
    
    # Print the contents of the deque
    def display(self):
        print(self.items)

# Example usage
if __name__ == "__main__":
    deque = Deque()
    
    # Add elements to the rear and front
    deque.add_rear(10)
    deque.add_rear(20)
    deque.add_front(5)
    deque.add_front(2)
    
    # Display the deque
    # deque.display()  # Output: [2, 5, 10, 20]
    print(deque.items)
    
    # Remove elements from front and rear
    print("Removed from front:", deque.remove_front())  # Output: 2
    print("Removed from rear:", deque.remove_rear())    # Output: 20
    
    # Display the deque again
    deque.display()  # Output: [5, 10]
    
    # Peek at front and rear
    print("Front item:", deque.peek_front())  # Output: 5
    print("Rear item:", deque.peek_rear())    # Output: 10
    
    # Check size of deque
    print("Deque size:", deque.size())  # Output: 2
