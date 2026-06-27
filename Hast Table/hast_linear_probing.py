class HashTable:
    def __init__(self):
        max_size = 10
        self.arr = [None for i in range(max_size)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 10
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,value)
        else:
            for i in range(len(self.arr)):
                if self.arr[i] is None:
                    self.arr[i] = (key,value)
                    return
            print("Error: Hash Table is full. Cannot insert new item.")
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        if self.arr[h] is not None and self.arr[h][0] == key:
            return self.arr[h][1]
        else:
            for i in range(len(self.arr)):
                if self.arr[i] is not None and self.arr[i][0] == key:
                    return self.arr[i][1]
            print("Error: Key not found in Hash Table.")
            return None
# check colision
h1 = HashTable()
h1["6"] = "John"
h1["17"] = "Doe"
print(h1.arr)


