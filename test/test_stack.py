import pytest
from src.stack import Stack


class TestStackBasicOperations:
    """Test basic stack operations: push, pop, peek."""
    
    def test_push_single_item(self):
        """Test pushing a single item onto the stack."""
        stack = Stack()
        stack.push(5)
        assert stack.size() == 1
        assert stack.peek() == 5
    
    def test_push_multiple_items(self):
        """Test pushing multiple items maintains LIFO order."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.size() == 3
        assert stack.peek() == 3
    
    def test_pop_single_item(self):
        """Test popping returns the top item."""
        stack = Stack()
        stack.push(10)
        result = stack.pop()
        assert result == 10
        assert stack.isEmpty()
    
    def test_pop_multiple_items_lifo(self):
        """Test popping multiple items follows LIFO order."""
        stack = Stack()
        stack.push('a')
        stack.push('b')
        stack.push('c')
        assert stack.pop() == 'c'
        assert stack.pop() == 'b'
        assert stack.pop() == 'a'
    
    def test_peek_does_not_remove(self):
        """Test peek views top without removing it."""
        stack = Stack()
        stack.push(42)
        assert stack.peek() == 42
        assert stack.size() == 1  # Item still there
        assert stack.peek() == 42  # Can peek again


class TestStackEmpty:
    """Test behavior with empty stack."""
    
    def test_isEmpty_on_new_stack(self):
        """Test new stack is empty."""
        stack = Stack()
        assert stack.isEmpty() is True
    
    def test_isEmpty_after_push(self):
        """Test isEmpty returns False after push."""
        stack = Stack()
        stack.push(1)
        assert stack.isEmpty() is False
    
    def test_isEmpty_after_pop_all(self):
        """Test isEmpty returns True after popping all items."""
        stack = Stack()
        stack.push(1)
        stack.pop()
        assert stack.isEmpty() is True
    
    def test_size_on_empty_stack(self):
        """Test size returns 0 for empty stack."""
        stack = Stack()
        assert stack.size() == 0
    
    def test_pop_empty_stack_raises_error(self):
        """Test pop on empty stack raises IndexError."""
        stack = Stack()
        with pytest.raises(IndexError, match="Empty Stack"):
            stack.pop()
    
    def test_peek_empty_stack_raises_error(self):
        """Test peek on empty stack raises IndexError."""
        stack = Stack()
        with pytest.raises(IndexError, match="Empty Stack"):
            stack.peek()


class TestStackDataTypes:
    """Test stack works with various data types."""
    
    def test_push_integers(self):
        """Test stack handles integers."""
        stack = Stack()
        stack.push(1)
        stack.push(-5)
        stack.push(0)
        assert stack.pop() == 0
    
    def test_push_floats(self):
        """Test stack handles floats."""
        stack = Stack()
        stack.push(3.14)
        stack.push(2.71)
        assert stack.pop() == 2.71
    
    def test_push_strings(self):
        """Test stack handles strings."""
        stack = Stack()
        stack.push("hello")
        assert stack.peek() == "hello"
    
    def test_push_none(self):
        """Test stack handles None values."""
        stack = Stack()
        stack.push(None)
        assert stack.peek() is None
    
    def test_push_mixed_types(self):
        """Test stack handles mixed data types."""
        stack = Stack()
        stack.push(42)
        stack.push("string")
        stack.push(3.14)
        assert stack.pop() == 3.14
        assert stack.pop() == "string"
        assert stack.pop() == 42
    
    def test_push_dictionaries(self):
        """Test stack handles complex objects."""
        stack = Stack()
        data = {"operation": "add", "result": 10}
        stack.push(data)
        assert stack.peek() == data


class TestStackSize:
    """Test size tracking."""
    
    def test_size_increases_with_push(self):
        """Test size increases correctly with each push."""
        stack = Stack()
        for i in range(5):
            stack.push(i)
            assert stack.size() == i + 1
    
    def test_size_decreases_with_pop(self):
        """Test size decreases correctly with each pop."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        assert stack.size() == 2
        stack.pop()
        assert stack.size() == 1


class TestStackSequences:
    """Test complex sequences of operations."""
    
    def test_push_pop_push_sequence(self):
        """Test alternating push and pop operations."""
        stack = Stack()
        stack.push(1)
        stack.pop()
        stack.push(2)
        assert stack.peek() == 2
    
    def test_large_number_of_operations(self):
        """Test stack with many operations."""
        stack = Stack()
        for i in range(100):
            stack.push(i)
        assert stack.size() == 100
        for i in range(99, -1, -1):
            assert stack.pop() == i
        assert stack.isEmpty()