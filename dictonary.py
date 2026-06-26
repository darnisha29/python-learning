# python internally use hash table to implement dictionary. 
# Hash table is a data structure that maps keys to values.
#  It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.


class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [ [] for i in range(self.max)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h%10
    
    def add(self,key,value):
        h  = self.get_hash(key)
        self.arr[h] = value
        return
    def __setitem__(self,key,value):
        h  = self.get_hash(key)
        Found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                Found = True
                break
        if Found == False:
            self.arr[h].append((key,value))
    
    def get(self,key):
        print("key is ",key)
        h = self.get_hash(key)
        print("hash is ",h)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        print("Not Found")
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        print("Not Found")
        
h1 = HashTable()
# h1.add('9799',"Anjali")
# value = h1.get('9799')
# print(value)
print(h1.get_hash('march 6'))
print(h1.get_hash('march 17'))
h1['march 6']  = "Darnisha"
h1['march 17']  = "Khushi"
h1["march 17"] = "Anjali"
print(h1['march 17'])
# print(h1['march 6'])
print(h1.arr)