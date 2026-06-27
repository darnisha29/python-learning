
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self,data):
        if self.head is None:
            print("first elem")
            node = Node(data)
            self.head = node
            print(self.head )
            return
        
        next = self.head
        print("second elem")
        node = Node(data,next)
        self.head = node
        print("self.head",self.head)
        
    def insertAtEnd(self,data):
        if self.head is None:
            node = Node(data)
            self.head = node
            print(self.head )
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data)
        
    def insert_values(self,data_values):
        self.head = None
        for data in data_values:
            self.insertAtEnd(data)
            
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
        
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
        itr = itr.next
        
    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
            
            
        if index == 0:
            self.insertAtBeginning(data)
            return
        
        
        itr = self.head
        count = 0
        while itr:
            
            if count == index-1:
                next = itr.next
                itr.next = Node(data,next)
                return
            itr = itr.next
            count +=1
            
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        
    def printLinkedlist(self):
        itr = self.head
        strll = ""
        
        
        while itr:
            strll = strll+ "--->" + str(itr.data) 
            itr = itr.next
        print(strll)
        
        
            
n1 = LinkedList()
# n1.insertAtBeginning(8)
# n1.insertAtBeginning(29)
n1.insert_values(["Khushi","Anjali","Urvashi","Chetan"])
n1.printLinkedlist()
# print("Length :: ",n1.get_length())
# n1.insert_at(4,"uhumiyu")
# n1.insert_after_value("Urvashi","Darnisha")
n1.remove_by_value("Khushi")
n1.printLinkedlist()
n1.remove_by_value("Urvashi")
n1.printLinkedlist()
print("Length :: ",n1.get_length())

        
        