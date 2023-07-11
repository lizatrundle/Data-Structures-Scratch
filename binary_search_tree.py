''' basic rules for any / (most) tree function
    1. find one or more base cases 
    2. call the same function on left subtree 
    3. call the same function on the right subtree 
    4. join the results
'''

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None 
    
def insert(self,root,val):
    if root is None:
        return Node(val) # return the newly created root of the tree 
    if val<root.key:
        root.left = insert(self,root.left,val)
    elif val>root.key:
        root.right = insert(self,root.right,val)
    return root #After inserting the node recursively in the left or right subtree, you should return the modified root to update the tree correctly. 
# you are essentially recreating the tree by inserting the new node, so thats why you have to set the 
# root left and right == the function call. the recursion goes down the two branches and when you return 
# root at the end (once you find a spot to put it) you create a new node and then you return the new root 

def search(self,root,val):
    if root is None or root.val==val:
        return root
    if val<root.val:
        return search(self,root.left,val)
    elif val>root.val:
        return search(self,root.right,val)
    # you need the return statement: if you dont have it then the function doesnt return the result 
    # of the recursive call back to the original caller 


def delete(self,root,val):
    if root is None:
        return None #--> there is no tree given to us
    
    if root.val == val:
        # four options: no children,left child, right child, two children
        if not root.left and not root.right:
            return None #get rid of the node 
        if not root.left and root.right:
            return root.right #taking the right node to replace 
        if not root.right and root.left:
            return root.left 
        
        # ino rder sucessor --> go right once and then left as far as possibel to get the greatest number 
        if root.left and root.right:
            # first go right
            pointer = root.right
            # while this pointer has a left, keep making a left traversal 
            while pointer.left: 
                pointer = pointer.left
            root.val = pointer.val # replace the node with the inorder sucessor 
            root.right = delete(root.right,root.val)

    elif root.val > val:
        root.left = delete(root.left, val)
    
    else:
        root.right = delete(root.right, val)

    return root

def inorder(self,root):
    # make sure root is not None
    if root is not None:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def preorder(self,root):
    if root is not None:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(self,root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

def inorder_iterate(self,root):
    stack = []
    curr = root
    while curr or stack:
        # Reach the leftmost node of the current subtree
        while curr:
            stack.append(curr)
            curr=curr.left
        # pop the most recently added node to the queue and visit it ( the bottom node)
        curr = stack.pop()
        print(curr.val, end="")
        # move to the right subtree 
        curr = curr.right

def preorder_iterate(self,root):
    stack = [root]
    while stack:
        curr = stack.pop()
        print(curr.val, end="")
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
            #pop the left first 

def postorder_iterate(self,root):
    stack1 = [root]
    stack2 = []
    while stack1:
        curr = stack1.pop()
        stack2.append(curr)
        if curr.left:
            stack1.append(curr.left)
        if curr.right:
            stack1.append(curr.right)
    while stack2:
        node = stack2.pop()
        print(node.val, end="")
        

def leaf_nodes(self,root):
    if root is None:
        return 0 
    if root.left is None and root.right is None:
        return 1
    return leaf_nodes(root.left)+ leaf_nodes(root.right)


def num_nodes(self,root):
    if root is None:
        return 0
    return 1 + num_nodes(root.left)+ num_nodes(root.right)

def reverse_tree(self,root):
    if root is None:
        return 
    else:
        reverse_tree(root.left)
        reverse_tree(root.right)
        root.left, root.right = root.right,root.left 


# valid range (starting from [-INFINITY, INFINITY]) and keep shrinking
def determine_bst(self,root, minimum, maximum):
  # Base case. An empty tree is a BST.
  if root == None:
    return True
  # Checking if a key is outside the permitted range.
  if root.val <= minimum:
    return False
  if root.val >= maximum:
    return False
  # Sending in updates ranges to the right and left subtree
  return determine_bst(root.right, root.val, maximum) and determine_bst(root.left,minimum, root.data)


# inorder sucessor --> the smallest key greater than the current value 
# the largest key in the BST is the node that is visited last in the inorder traversal 
# two cases:
# 1. the right subtree of x is not empty 
#     - then the inorder sucessor will be the leftmost node in the right subtree 

# 2. the right subtree of x is empty 
#     - the inorder sucessor is the lowest ancestor of x whose left child is also an ancestor of x 
#     - move up the tree from x until we find a node that is the left child of x's parent
def inorder_sucessor(self,root,node):
    # if root.right is not None:
    #     return min_val(self,node)
    sucessor = None
    while root:
        # if the nodes val is greater than the current val, then we want to go into the right subtree
        if node.val >= root.val:
            root=root.right # enter right subtree 
        else: # it is a potential sucessor 
            sucessor = root 
            root = root.left 
    return sucessor 
# brute force solution --> perform an inorder traversal of the BST, then index into the list 

def inorder_predecessor(self,root, node):
    predecessor = None
    while root:
        if node.val <= root.val:
            root=root.left
        else:
            predecessor = root 
            root = root.right
    return predecessor 


# min val is leftmost in the tree 
def min_val(self,root):
    while root.left:
        root = root.left
    return root

def max_val( self,root):
    while root.right:
        root=root.right
    return root


#lowest common ancestor = defined between two nodes p and q is the lowest node in the tree that has both p and q as descendants 
# root is the common ancestor of every single node, we want to possibly find one thats lower in the tree
def lca(self,p,q):
    while True:
        # if the nodes are greater than the root, the LCA is in the right subtree
        if root.val < min(p.val,q.val):
            root = root.right
        # if the nodes are less than the root, the LCA is in the right subtree
        elif root.val > max(p.val,q.val):
            root = root.left
        else:
        # if the root is dividing the two nodes, then the LCA must be the root 
            return root


def identical_trees(self,x,y):
    if x is None and y is None:
        return True 
    if x is not None and y is not None:
        return x.val == y.val and identical_trees(x.left,y.left) and identical_trees(x.right,y.right)


def kth_smallest_iter(self,root,k):
    #do an inorder and keep track of what nodes we are visiting 
    # stack contains prev nodes we need to pop back to 
    num_visited = 0 # once n == k, we know we can stop 
    stack = []
    curr = root # which node we are at 
    while curr and stack:
        while curr:
            stack.append(curr)
            # remember that inorder looks at bottom left first 
            curr = curr.left # break out once you hit the bottom left node
        curr = stack.pop() # then pop back up to the parent 
        num_visited +=1 # mark that one you popped as a node visited 
        if num_visited == k: # check if you are at the kth smallest 
            return curr.val
        curr = curr.right # if not, check the right child (left, root, right)

def kth_largest_iter(self,root,k):
    num_visited = 0 
    stack = []
    curr = root 
    while curr and stack:
        while curr:
            stack.append(curr)
            curr = curr.right # go to rightmost node 
        curr = stack.pop() # pop the parent 
        num_visited +=1 
        if num_visited == k: 
            return curr.val
        curr = curr.left #(reverse inorder (right root left --> this will give you the nodes in decreasing order ))



 # brute force solution just do inorder and then index 
def kth_smallest_node_bf(self,root,k):
    def tree_to_list(root) -> list:
        if not root:
            return []

        return tree_to_list(root.right) + [root.val] + tree_to_list(root.left)
    
    tree_list = tree_to_list(root)
    return tree_list[-k]

def kth_largest_node_bf(self,root,k):
    def tree_to_list(root) -> list:
        if not root:
            return []

        return tree_to_list(root.left) + [root.val] + tree_to_list(root.right)
    
    tree_list = tree_to_list(root)
    return tree_list[-k]

