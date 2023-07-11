class Queue:
    def __init__(self):
        # Initializing the stacks
        self.s1 = []
        self.s2 = []
 
    # Function to implement enqueue
    def enqueue(self, element):
        # Pushing element in the stack
        self.s1.append(element)

    def empty(self):
        if (len(self.s1) == 0 and len(self.s2) == 0):
            return True
        return False
        
 
    # Function to implement dequeue operation 
    def dequeue(self):
        # Condition where the queue is empty
        if self.empty():
            print("the queue is Empty")
            return
 
        elif (len(self.s2) == 0 and len(self.s1) > 0):
            while len(self.s1):
                element = self.s1.pop()
                self.s2.append(element)
            return self.s2.pop()
 
        else:
            # Popping the top element from the stack
            return self.s2.pop()
        

if __name__ == "__main__":
    s = Queue()
    s.enqueue(5)
    s.enqueue(6)
    s.enqueue(8)
    print(s.s1)
    s.dequeue()
    print(s.s2)
    # s.pop()
    # s.pop()
    # print(s)