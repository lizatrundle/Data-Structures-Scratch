#!/usr/bin/python3

class Queue:

    def __init__(self):
        self.queue = []
 
   
    def enqueue(self, value):
        # add to queue (adds to the back)
        self.queue.append(value)

    def dequeue(self):
        # remove item from the queue: in the order that it is pushed 
        self.queue.pop(0)
    
    def front(self):
        # get front item from the queue 
        return self.queue[0]

    def rear(self):
        # return the end of the queue (most recently added)
        return self.queue[len(self.queue)-1]

    def isempty(self):
        return True if len(self.queue)==0 else False
    
    

    
 
if __name__ == "__main__":
    s = Queue()
    s.enqueue(5)
    s.enqueue(6)
    s.enqueue(8)
    print(s.queue)
    s.dequeue()
    print(s.queue)
    # s.pop()
    # s.pop()
    # print(s)