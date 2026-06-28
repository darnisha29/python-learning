# Design a food ordering system where your python program will run two threads,

# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.



from collections import deque
import threading
import time

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    

order_queue = Queue()  

def place_order(orders):
   
    for order in orders:
        
        print("Placing order: ", order)
        order_queue.enqueue(order)
        time.sleep(0.5)
    
    
def serve_order():
    time.sleep(1)
    while not order_queue.is_empty():
       
        order = order_queue.dequeue()
        print("Processing order: ", order)
        time.sleep(2)


t = time.time()

t1 = threading.Thread(target=place_order, args=(["pizza", "pasta", "burger", "soda"],))
t2 = threading.Thread(target = serve_order)

t1.start()
t2.start()

t1.join()
t2.join()

print("Time taken: ", time.time()-t)
print("All orders have been processed.")