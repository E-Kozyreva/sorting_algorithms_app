class Node(object):

    def __init__(self, key: int):
        self.key = key
        self.left = None 
        self.right = None 


class AVLTree(object):

    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)

                
    def height(self) -> int:
        return self.node.height if self.node else 0
    

    def is_leaf(self) -> bool:
        return (self.height == 0) 
    

    def insert(self, key: int) -> bool:
        tree = self.node
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
        elif key < tree.key: 
            self.node.left.insert(key)
        elif key > tree.key: 
            self.node.right.insert(key)
        self.rebalance() 
        
    
    def rebalance(self) -> None:
        self.update_heights(False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() 
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() 
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


    def rrotate(self) -> None:
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self) -> None:
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 

    
    def rl_rotate(self) -> None:
        self.node.right.rrotate()
        self.lrotate()

    
    def lr_rotate(self) -> None:
        self.node.left.lrotate()
        self.rrotate()
        
            
    def update_heights(self, recurse=True) -> None:
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            self.height = max(self.node.left.height, self.node.right.height) + 1 
        else: 
            self.height = -1 

       
    def update_balances(self, recurse=True) -> None:
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()
            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 


    def delete(self, key: int) -> None:
        if self.node != None: 
            if self.node.key == key: 
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None:
                        self.node.key = replacement.key 
                        self.node.right.delete(replacement.key)
                self.rebalance()
                return  
            elif key < self.node.key: 
                self.node.left.delete(key)  
            elif key > self.node.key: 
                self.node.right.delete(key)
            self.rebalance()
        else: 
            return 


    def logical_predecessor(self, node):
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    

    def logical_successor(self, node):
        node = node.right.node  
        if node != None:  
            while node.left != None:
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 


    def check_balanced(self) -> bool:
        if self == None or self.node == None: 
            return True
        
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        

    def inorder_traverse(self) -> list:
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 
