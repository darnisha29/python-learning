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
            print("in left in_order_traversal :: ",self.left.data)
            elements += self.left.in_order_traversal()
            

        print("base element adding :: ",self.data)
        elements.append(self.data)
        
        if self.right:
            print("in right in_order_traversal :: ",self.right.data)
            elements += self.right.in_order_traversal()
            
        return elements
        
def build_tree(elements):
    root = BinaryTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
        
    return root
    

if __name__ == '__main__':
    elements = [17,4,1,20,9,23,18,34]
    numbers_tree = build_tree(elements)
    print(numbers_tree.in_order_traversal())
    
    
    