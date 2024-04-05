# Design a class to implement a stack using only a single queue. Your class, QueueStack, should support the following stack methods: push() (adding an item), pop() (removing an item), peek() (returning the top value without removing it), and empty() (whether or not the stack is empty).

class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.size = 0
    
    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        popped = self.queue.pop(0)
        self.size -= 1
        return popped
        
    def display(self):
        print(self.queue)
        return self.queue

class QueueStack:
    def __init__(self) -> None:
        self.queue = Queue()
    
    def push(self, item):
        if self.queue.size < 1:
            self.queue.enqueue(item)
            return
        
        self.queue.enqueue(item)
        
        for i in range(self.queue.size - 1):
            self.queue.enqueue(self.queue.dequeue())
        pass
    
    def pop(self):
        self.queue.dequeue()
    
    def peek(self):
        print(self.queue.queue[0])
        return self.queue.queue[0]
    
    def empty(self):
        size = self.queue.size
        if size < 1:
            print('empty')
            return True
        
        return False
    

st = QueueStack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)

print("Top element: ", st.peek())  # Output: 4
print("Is stack empty? ", st.empty())  # Output: False
print("Popping")
print("Top element after pop: ", st.peek())  # Output: 3
print("Is stack empty after pop? ", st.empty())  # Output: False

