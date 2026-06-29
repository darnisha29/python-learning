class TreeNode:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        p = self.parent
        level = 0
        while p:
            p = p.parent
            level += 1
        return level
    
    def print_tree(self):
        space = self.get_level()
        level =  ' ' * space * 3 
        prefix = level + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_tree() 
        
    

def build_product_tree():
    root= TreeNode("Electronic")
    
    laptop = TreeNode("Laptop")
    
    root.add_child(laptop)
    
    mac = TreeNode("Mac")
    asus = TreeNode("Asus")
    
    laptop.add_child(mac)
    laptop.add_child(asus)

    root.print_tree()
    
build_product_tree()

    

    