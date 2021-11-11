class Tree:
    """Abstract base class representing a tree structure"""
    class Position:
        """Abstraction representing the location of a single element"""
        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError('must be implemented by subclass')
        
        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not respresent the same location"""
            return not (self == other)
        
        # ---------- abstract methods that concrete subclass must support ----------
        
        def root(self):
            """Return the position respresenting the root, None if empty"""
            raise NotImplementedError('must be implemented by subclass')

        def parent(self, p):
            """Return Position respresenting the root of tree, None if p == root"""
            raise NotImplementedError('must be implemented by subclass')

        def num_children(self, p):
            """Return the number of children that Position p has"""
            raise NotImplementedError('must be implemented by subclass')

        def children(self, p):
            """Generate an iteration of Positions representing p's children"""
            raise NotImplementedError('must be implemented by subclass')

        def __len__(self):
            """Return total number of elements in the tree"""
            raise NotImplementedError('must be implemented by subclass')
        
        # ---------- concrete methods implemented in this class ----------

        def is_root(self, p):
            """Return true if p is the root"""
            return self.root() == p
        
        def is_leaf(self, p):
            """Return true if p doesn't have any children"""
            return self.num_children(p) == 0

        def is_empty(self):
            """Return true if tree is empty"""
            return len(self) == 0