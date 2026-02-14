# Calculator with Undo/Redo

## Description

Build a command-line calculator that performs basic arithmetic operations with full undo/redo functionality. This project reinforces fundamental data structure knowledge by requiring a custom stack implementation (not using Python's built-in list methods directly) to manage operation history. The focus is on understanding how stacks enable state management, writing comprehensive unit tests, and analyzing time/space complexity.

## Learning Objectives

- Implement stack data structure from scratch
- Apply stack to solve a real-world problem (undo/redo)
- Practice test-driven development with pytest
- Document and analyze algorithmic complexity
- Build confidence with fundamental CS concepts

## Acceptance Criteria

### Core Calculator
- [ ] Performs basic operations: add, subtract, multiply, divide
- [ ] Handles decimal numbers
- [ ] Validates input (prevents division by zero, invalid operations)
- [ ] Returns results correctly

### Stack Implementation
- [ ] Custom stack class implemented from scratch (no using built-in list as-is)
- [ ] Push and pop operations work correctly
- [ ] Peek operation to view top without removing
- [ ] Stack properly tracks its size/isEmpty state

### Undo Functionality
- [ ] Each calculation result is pushed to undo stack
- [ ] Undo restores previous calculation result
- [ ] Multiple consecutive undos work correctly
- [ ] Cannot undo beyond initial state

### Redo Functionality
- [ ] Redo stack stores undone operations
- [ ] Redo restores the calculation that was undone
- [ ] Redo stack clears when new calculation is performed
- [ ] Cannot redo when redo stack is empty

### Testing
- [ ] Unit tests for all stack operations
- [ ] Unit tests for all calculator operations
- [ ] Unit tests for undo/redo edge cases (empty stacks, multiple operations)
- [ ] At least 80% code coverage

### Documentation
- [ ] Time complexity documented for each stack operation
- [ ] Space complexity documented for undo/redo system