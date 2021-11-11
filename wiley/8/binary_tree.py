class BinaryTree:
    """Abstract base class representing a binary tree structure"""

# --------------------- additional abstract methods ---------------------

    def left(self, p):
        """Return a Position representing p's left child, None if left child doesn't exist"""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's left child, None if left child doesn't exist"""
        raise NotImplementedError('must be implemented by subclass')
    

# ---------- concrete methods implemented in this class ----------

    def sibling(self, p):
        """Return a position representing p's sibling, None if no siblings"""
        parent = self.parent(p)
        #no parent must mean p is root
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
        
    def children(self, p):
        """Generate iteration of Positions of p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
        """Return sends a specified value back to its caller
           whereas Yield can produce a sequence of values. 
           We should use yield when we want to iterate over a sequence
           but don’t want to store the entire sequence in memory."""

