class Node:
    """node of a linked list"""
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """get node data"""
        return self._data

    def set_data(self, node_data):
        """set node data"""
        self._data = node_data
    
    data = property(get_data, set_data)
    
    def get_next(self):
        """get next node"""
        return self._next

    def set_next(self, node_next):
        """set next node"""
        self._next = node_next
    
    next = property(get_next, set_next)

    def __str__(self):
        """string"""
        return str(self._data)
