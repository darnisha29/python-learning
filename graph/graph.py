
class Graph:
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        for start , end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("graph_dict :: ",self.graph_dict)
        
    def get_paths(self,start,end,path=[]):
        path = path + [start]
        
        if start == end:
            return [path]
            
        if start not in self.graph_dict:
            return []
            
        paths = []
        for node in self.graph_dict[start]:
            if node  not in path:
               new_paths =  self.get_paths(node,end,path)
               for p in new_paths:
                   paths.append(p)
                 
        return paths
        
    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]
            
        if start == end:
            return path
                
        if start not in self.graph_dict:
            return []
            
        new_path = []
        
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node,end,path)
            if  new_path == [] or len(sp) < len(new_path):
                new_path = sp
                    
        return new_path

if __name__ == '__main__':
    routes = [
        ("mumbai","paris"),
        ("mumbai","dubai"),
        ("paris","dubai"),
        ("paris","newyork"),
        ("dubai","newyork"),
        ("newyork","torento")
        ]
    route_graph = Graph(routes)
    print("total paths :: ",route_graph.get_paths("mumbai","newyork"))
    print("shortest path :: ",route_graph.get_shortest_path("mumbai","newyork"))
    