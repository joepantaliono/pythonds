class Deque():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """check if deque is empty"""
        return not self.items
    
    def add_front(self, item):
        """add to front of deque"""
        self.items.append(item)

    def add_rear(self, item):
        """add to rear of list"""
        self.items.insert(0, item)

    def remove_front(self):
        """remove from front of deque"""
        return self.items.pop()

    def remove_rear(self):
        """remove from rear"""
        return self.items.pop(0)

    def view(self):
        """view current state of deque"""
        return self.items
    
    def size(self):
        """return size of deque"""
        return len(self.items)
    

    


my_deque = Deque()
my_deque.add_front(8)
my_deque.add_front(4)
my_deque.add_front(32)
my_deque.view() # [8,4,32]
my_deque.is_empty() #false
my_deque.add_rear(22)
my_deque.add_rear(14)
my_deque.add_rear(66)
my_deque.view() #[66,14,22,8,4,32]
my_deque.size() #[6]
my_deque.remove_front()
my_deque.remove_rear()
my_deque.view() #[14,22,8,4]

