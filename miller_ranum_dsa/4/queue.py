class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """check if queue is empty"""
        if len(self.items) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        """add item to end of queue"""
        self.items.insert(0, item) # insert requires index as first arg
        # each enqueue will insert at index 0, making 0 the "rear of the queue"

    def dequeue(self):
        """remove item from front of queue"""
        return self.items.pop()
        # pop from index n-1, "front of queue"

    def size(self):
        """return num items in queue"""
        return len(self.items)
    
    def view(self):
        """view entire queue"""
        return self.items

my_queue = Queue()
my_queue.enqueue(4)
my_queue.enqueue(36)
my_queue.enqueue(12)
my_queue.enqueue(3)
my_queue.is_empty() # false
my_queue.view() # [3, 12, 36, 4]
my_queue.size() # 4
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
print(my_queue.is_empty()) # true
my_queue.view() # []