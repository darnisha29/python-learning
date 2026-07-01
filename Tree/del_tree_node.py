class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if self.data  == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def in_order_traversal(self):
        elements = []
        
        
        if self.left:
            elements += self.left.in_order_traversal()
            

        elements.append(self.data)
        
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
        
    def pre_order_traversal(self):
        elements = []
        
        elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()
            
        return elements
     
    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements += self.right.post_order_traversal()
            
        elements.append(self.data)
        
        return elements
    
    def find_minimum(self):
        if self.left is None:
            return self.data
        return self.left.find_minimum()

    def find_maximum(self):
        if self.right is None:
            return self.data
        return self.right.find_maximum()
    
    def calculate_sum(self):
        
        left_sum = self.left.calculate_sum() if self.left else 0
        print("left_sum :: ",left_sum)
        right_sum = self.right.calculate_sum() if self.right else 0
        print("right_sum :: ",right_sum)
        return self.data + left_sum + right_sum
    
    def delete(self,value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_value = self.right.find_minimum()
            self.data = min_value
            self.right = self.right.delete(min_value)
        
        return self
         
        
        
def build_tree(elements):
    root = BinaryTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
        
    return root
    

if __name__ == '__main__':
    elements = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(elements)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.delete(9))
    print(numbers_tree.in_order_traversal())