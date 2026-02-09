class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, data):
        """Add an item to the top of the stack."""
        self.items.append(data)

    def pop(self):
        """Remove and return the top item from the stack."""
        if len(self.items) == 0:
            raise IndexError("Empty Stack")
        return self.items.pop()
    
    def peek(self):
        """View the top item without removing it."""
        if len(self.items) == 0:
            raise IndexError("Empty Stack")
        return self.items[-1]
    
    def size(self):
        """Get the number of items in the stack."""
        return len(self.items)
    
    def isEmpty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    