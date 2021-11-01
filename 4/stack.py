class Stack:
    def __init__(self):
        """create a new stack"""
        self.items = []

    def is_empty(self):
        """check if the stack is empty"""
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        """push an item on top of stack"""
        self.items.append(item)

    def pop(self):
        """pop off top of stack"""
        self.items.pop()

    def peek(self):
        """view top item of stack"""
        return self.items[-1]

    def size(self):
        """return size of stack"""
        return len(self.items)

    def view(self):
        """print entire stack"""
        return self.items

my_stack = Stack()
Stack.is_empty(my_stack) # true
my_stack.push(7)
my_stack.push(14)
my_stack.push(6)
my_stack.push(34)
Stack.is_empty(my_stack) # false
Stack.peek(my_stack) #34
Stack.pop(my_stack)
Stack.peek(my_stack) #6
Stack.size(my_stack) #3
Stack.view(my_stack) #[7,14,6]
Stack.push(my_stack, 35)
Stack.view(my_stack) #[7,14,6,35]