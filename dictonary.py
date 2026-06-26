# python internally use hash table to implement dictionary. 
# Hash table is a data structure that maps keys to values.
#  It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.


class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]
    
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h%100
    
    def add(self,key,value):
        h  = self.get_hash(key)
        self.arr[h] = value
        return
    def __setitem__(self,key,value):
        h  = self.get_hash(key)
        self.arr[h] = value
        return
    
    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
        
h1 = HashTable()
h1.add('9799',"Anjali")
value = h1.get('9799')
print(value)

h1['2910']  = "Darnisha"
print(h1['2910'])