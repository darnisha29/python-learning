class TreeNode:
    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
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

    def print_tree(self, property_name):
        space = self.get_level()
        level = ' ' * space * 3
        prefix = level + "|__" if self.parent else ""
        if property_name == "name":
            print(prefix + self.name)
        elif property_name == "designation":
            print(prefix + self.designation)
        elif property_name == "both":
            print(prefix + self.name + " (" + self.designation + ")")
        for child in self.children:
            child.print_tree(property_name)

def build_management_tree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    infra_head = TreeNode("Vishwa", "Infrastructure Head")
    cto.add_child(infra_head)
    app_head = TreeNode("Aamir", "Application Head")
    cto.add_child(app_head)

    hr_head = TreeNode("Gels", "HR Head")
    recruitment_manager = TreeNode("Peter", "Recruitment Manager")
    hr_head.add_child(recruitment_manager)
    policy_manager = TreeNode("Waqas", "Policy Manager")
    hr_head.add_child(policy_manager)

    root.add_child(cto)
    root.add_child(hr_head)

    return root





# i want to call build_management_tree like showed below in main function so make existing code changes accordingly.   

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy


