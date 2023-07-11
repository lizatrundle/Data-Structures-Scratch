#!/usr/bin/python3

class Stack:

    def __init__(self):
        self.stack = []
 
   
    def push(self, value):
        # adds elements to the top of the stack
        # most recently added is at the top of the stack
        self.stack.append(value)

    def pop(self):
        # pops elements from the top of the stack in LIFO order
        # pops from end of the stack (most recently added goes fist)
        return self.stack.pop()
    
    def top(self):
        return self.stack[len(self.stack)-1]
    
    def isempty(self):
        return True if len(self.stack)==0 else False
    
    
    
 
if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(8)
    print(s.stack)
    # s.pop()
    # s.pop()
    # print(s)