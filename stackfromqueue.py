import myqueue


class StackFromQueue:
    def __init__(self):
        self.q = myqueue.Queue()
 
    def is_empty(self):
        return self.q.isempty()
 
    def push(self, data):
        self.q.enqueue(data)
 
    def pop(self):
        for _ in range(len(self.q.queue) - 1):
            dequeued = self.q.dequeue()
            self.q.enqueue(dequeued)
        return self.q.dequeue()




if __name__ == "__main__":
    s = StackFromQueue()
    s.push(5)
    s.push(6)
    s.push(8)
    s.push(1)
    s.push(2)
    s.push(3)
    
    # print(s.pop)
    s.pop()
    print(s.q)
    # s.pop()
    # s.pop()
    # print(s)