class TreeNode:
    def __init__(self,name):
        self.location = name
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

    def print_tree(self, level):
        space = self.get_level()
        l = ' ' * space * 3
        prefix = l + "|__" if self.parent else ""
        # i want to print node from root to level so i will pass level as argument and print node if level is less than or equal to passed level
        if space <= level:
            print(prefix + self.location)
        if space == level:
            return
        
        for child in self.children:
            child.print_tree(level)
       

def build_location_tree():
    root = TreeNode("Global")

    asia = TreeNode("Asia")
    india = TreeNode("India")
    india.add_child(TreeNode("Delhi"))
    india.add_child(TreeNode("Mumbai"))
    china = TreeNode("China")
    china.add_child(TreeNode("Beijing"))
    china.add_child(TreeNode("Shanghai"))
    asia.add_child(india)
    asia.add_child(china)

    europe = TreeNode("Europe")
    germany = TreeNode("Germany")
    germany.add_child(TreeNode("Berlin"))
    germany.add_child(TreeNode("Munich"))
    france = TreeNode("France")
    france.add_child(TreeNode("Paris"))
    france.add_child(TreeNode("Lyon"))
    europe.add_child(germany)
    europe.add_child(france)

    root.add_child(asia)
    root.add_child(europe)

    return root

if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(2)