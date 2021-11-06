from node import Node

class UnorderedList:
    """unordered list built from a collection of nodes"""
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """check if linked list is empty"""
        # if head points to null/none, there are no other nodes
        return self.head == None

    def add(self, item):
        """add new item to linked list"""
        temp = Node(item) # create new node and set item as its data
        temp.set_next(self.head) # if first node, we set next to None, indicating end of LL
        self.head = temp # new head points to new node
        # adding new node near the head will allow for traversal of newest nodes first (can only enter at head)

    def size(self):
        """traverse linked list and keep count of nodes"""
        current = self.head
        count = 0
        while current is not None: # is not checks pointers, whereas != would check equality.
            count = count + 1
            current = current.next
        return count

    def search(self, item):
        """search for an item in linked list, return True if found"""
        # traverse list and check if item == data
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        """remove node from linked list"""
        current = self.head
        previous = None
        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next