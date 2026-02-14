from src.stack import Stack

class Calculator:
    '''A calculator with undo/redo functionality using custom stacks.'''

    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()
        self.current_result = 0

    def calculate(self, value1, value2, operator):
        '''Perform a calculation and store in undo stack.'''
        
        # Validate Inputs
        if operator not in ["+", "-", "*", "/"]:
            raise ValueError(f"Invalid Operator: {operator}")
        
        if operator == "/" and value2 == 0:
            raise ValueError("Cannot divide by zero")
        
        # Store Previous Result Before Calculating
        self.undo_stack.push(self.current_result)

        # Clear Redo Stack When New Calculation is Performed
        self.redo_stack = Stack()

        # Perform Calculation
        if operator == "+":
            self.current_result = value1 + value2
        elif operator == "-":
            self.current_result = value1 - value2
        elif operator == "*":
            self.current_result = value1 * value2
        elif operator == "/":
            self.current_result = value1 / value2

        return self.current_result
    
    def undo(self):
        '''Undo the last calculation.'''

        if self.undo_stack.isEmpty():
            raise IndexError("No operations to undo")
        
        # Store Current Result in Redo Stack
        self.redo_stack.push(self.current_result)

        # Restore Previous Result
        self.current_result = self.undo_stack.pop()

        return self.current_result
    
    def redo(self):
        '''Redo the last undone calculation.'''

        if self.redo_stack.isEmpty():
            raise IndexError("Cannot redo when redo stack is empty")
        
        # Store Current Result in Undo Stack
        self.undo_stack.push(self.current_result)

        # Restore the Result that was Done
        self.current_result = self.redo_stack.pop()

        return self.current_result
    
    def get_result(self):
        '''Get the current result without modifying state.'''

        return self.current_result
        