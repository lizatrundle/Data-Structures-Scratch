class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None 



class Single:
    def __init__(self):
        self.head = None
 

    def print(self):
        cur = self.head
        while cur.next:
            print(cur.val)
            cur = cur.next

    def find(self,val):
        cur = self.head
        while cur.next:
            if cur.val == val:
                return cur 
            cur = cur.next
        return None

    def insert_at_end(self,val):
        cur = self.head
        while cur.next:
            cur = cur.next 
        cur.next = Node(val)

    def insert_at_front(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def delete(self,val):
        cur = self.head
        while cur.val is not val:
            cur = cur.next # keep moving the list forward until you find the value of what you want to delete 
        cur.val = cur.next.val # replace value to be deleted with the next value 
        cur.next = cur.next.next # replace pointer

    def check_cycle(self):
        # two pointers technique 
        slow = self.head
        fast = self.head
        # keep going until the fast pointer reaches the end 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if fast == slow: # fast is moving at double speed, if it catches the slow pointer ever then it has a cycle 
                return True 
        return False 


    #list guaranteed to be sorted 
    def delete_duplicates(self):
        curr = self.head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return self.head
    
    def reverse_list(self):
        prev = None
        curr = self.head 
        while curr:
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        # swapping in place, then returning the list as a whole 
        return prev
    
    def is_palindrome(self):
        # easy way = iterate through the list and add to array, then index the array to check if palindrome 
        if not self.head or not self.head.next:
            return True 
        
        # find the midpoint of the linked list 
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        # reverse the second half of the linkedlist 
        prev = None 
        curr = slow 
        while curr:
            next_node = curr.next
            curr.next = prev 
            prev = curr
            curr = next 
        
        # see if the two halves are equal 
        p1 = self.head 
        p2 = prev
        while p2:
            if p1.val!= p2.val:
                return False
            p1 = p1.next 
            p2 = p2.next
        
        return True 



def merge_two_lists(list1,list2):
    head = Node()
    curr = head
    # iterate through while both of them arent null --> if they arent the same size then check at the end for remaining elements 
    while list1 and list2:
        if list1.val <list2.val:
            curr.next = list1
            list1=list1.next 
        else:
            curr.next = list2
            list2=list2.next
        curr == curr.next

    curr.next = list1 or list2 # same as checking which is null
    
    return head.next
# return head next because we dont want to include the empty node
# you cant return curr.next because its pointing at the tail of the list right now 










           
