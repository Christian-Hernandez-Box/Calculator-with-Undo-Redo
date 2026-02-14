# Time and Space Complexity Analysis

## Stack Implementation

### Push Operation
```python
def push(self, data):
    self.items.append(data)
```
- **Time Complexity**: O(1) amortized
- **Explanation**: Python's list append operation is O(1) amortized. While occasional resizing occurs when the list reaches capacity, the cost is distributed across many operations.
- **Space Complexity**: O(1) for the operation itself (adds one element)

### Pop Operation
```python
def pop(self):
    if len(self.items) == 0:
        raise IndexError("Empty Stack")
    return self.items.pop()
```
- **Time Complexity**: O(1)
- **Explanation**: Python's list pop (from end) is O(1) because it only removes the last element without shifting other elements.
- **Space Complexity**: O(1) (no additional space needed)

### Peek Operation
```python
def peek(self):
    if len(self.items) == 0:
        raise IndexError("Empty Stack")
    return self.items[-1]
```
- **Time Complexity**: O(1)
- **Explanation**: Accessing the last element via index in a list is constant time.
- **Space Complexity**: O(1)

### isEmpty Operation
```python
def isEmpty(self):
    return len(self.items) == 0
```
- **Time Complexity**: O(1)
- **Explanation**: len() on a Python list is O(1) - the size is cached.
- **Space Complexity**: O(1)

### Size Operation
```python
def size(self):
    return len(self.items)
```
- **Time Complexity**: O(1)
- **Explanation**: len() returns the cached length of the list.
- **Space Complexity**: O(1)

---

## Stack Overall Space Complexity
- **Space Complexity**: O(n) where n is the number of elements stored
- **Explanation**: The underlying list grows linearly with the number of pushed elements.

---

## Calculator Implementation

### Calculate Operation
```python
def calculate(self, value1, value2, operator):
    # Validation: O(1)
    # Push to undo_stack: O(1)
    # Arithmetic operation: O(1)
    # Clear redo_stack: O(1)
```
- **Time Complexity**: O(1)
- **Explanation**: 
  - Input validation is constant (checking operator and division by zero)
  - Stack push is O(1) amortized
  - Arithmetic operations are O(1)
  - Creating a new stack for redo is O(1)
  
- **Space Complexity**: O(1) per operation
- **Note**: While undo_stack grows with each calculation, each individual calculate() call uses O(1) additional space

### Undo Operation
```python
def undo(self):
    if self.undo_stack.isEmpty():
        raise IndexError("No operations to undo")
    self.redo_stack.push(self.current_result)  # O(1)
    self.current_result = self.undo_stack.pop()  # O(1)
```
- **Time Complexity**: O(1)
- **Explanation**: Both stack operations (push and pop) are O(1).
- **Space Complexity**: O(1)
- **Note**: Moves data between stacks but doesn't create new data

### Redo Operation
```python
def redo(self):
    if self.redo_stack.isEmpty():
        raise IndexError("Cannot redo when redo stack is empty")
    self.undo_stack.push(self.current_result)  # O(1)
    self.current_result = self.redo_stack.pop()  # O(1)
```
- **Time Complexity**: O(1)
- **Explanation**: Both stack operations (push and pop) are O(1).
- **Space Complexity**: O(1)

### Get Result Operation
```python
def get_result(self):
    return self.current_result
```
- **Time Complexity**: O(1)
- **Explanation**: Simple variable access.
- **Space Complexity**: O(1)

---

## Calculator Overall Space Complexity

### Per Calculator Instance
- **Space Complexity**: O(m) where m is the number of unique calculation states stored
- **Explanation**: 
  - Two stacks (undo and redo) store calculation history
  - Each state stores one float value (the result)
  - In worst case (all undos), m = n where n is total operations performed
  - In typical case, m ≤ n

### Example Scenario
```
Operations performed: 10
Undo operations: 5

undo_stack size: 5 (stores first 5 states: 0, result1, result2, result3, result4)
redo_stack size: 5 (stores last 5 states that were undone)
Total space: O(10) in worst case
```

### Memory Analysis
- **Per float value**: ~28 bytes (Python object overhead + value)
- **100 operations**: ~2.8 KB
- **1000 operations**: ~28 KB
- **10,000 operations**: ~280 KB

---

## Algorithm Complexity Summary

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Push | O(1) amortized | O(1) per element | List resizing amortized |
| Pop | O(1) | O(1) | No array shifting |
| Peek | O(1) | O(1) | Index lookup |
| isEmpty | O(1) | O(1) | Cached length |
| Size | O(1) | O(1) | Cached length |
| Calculate | O(1) | O(1) per operation | Validation + arithmetic |
| Undo | O(1) | O(1) | Two stack operations |
| Redo | O(1) | O(1) | Two stack operations |

---

## Comparison: Why Stack is Optimal

### Alternative: Using List.pop(0) (Wrong Approach)
```python
# Bad: Removing from front requires shifting all elements
def pop_wrong(self):
    return self.items.pop(0)  # O(n) - shifts all remaining elements!
```
- **Time Complexity**: O(n) - every pop must shift remaining elements
- **Why we don't do this**: 100 operations = 5,050 shifts total

### Our Approach: Using List.pop() (Correct)
```python
# Good: Removing from end is constant time
def pop(self):
    return self.items.pop()  # O(1) - no shifting needed
```
- **Time Complexity**: O(1) per operation
- **Total for 100 operations**: ~100 simple operations

---

## Conclusion

The stack-based undo/redo system achieves **optimal time complexity**:
- Every operation (calculate, undo, redo) is **O(1)**
- Total time for n operations: **O(n)**
- Space usage: **O(n)** - unavoidable since we must store history

This design allows users to perform unlimited undo/redo operations without degradation in performance.