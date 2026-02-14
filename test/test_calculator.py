import pytest
from src.calculator import Calculator


class TestCalculatorBasicOperations:
    """Test basic arithmetic operations."""
    
    def test_add(self):
        """Test addition operation."""
        calc = Calculator()
        result = calc.calculate(5, 3, '+')
        assert result == 8
        assert calc.get_result() == 8
    
    def test_subtract(self):
        """Test subtraction operation."""
        calc = Calculator()
        result = calc.calculate(10, 4, '-')
        assert result == 6
    
    def test_multiply(self):
        """Test multiplication operation."""
        calc = Calculator()
        result = calc.calculate(7, 6, '*')
        assert result == 42
    
    def test_divide(self):
        """Test division operation."""
        calc = Calculator()
        result = calc.calculate(20, 4, '/')
        assert result == 5.0
    
    def test_divide_floats(self):
        """Test division with decimal results."""
        calc = Calculator()
        result = calc.calculate(7, 2, '/')
        assert result == 3.5
    
    def test_negative_numbers(self):
        """Test operations with negative numbers."""
        calc = Calculator()
        result = calc.calculate(-5, 3, '+')
        assert result == -2
    
    def test_decimal_numbers(self):
        """Test operations with decimal numbers."""
        calc = Calculator()
        result = calc.calculate(3.5, 2.0, '*')
        assert result == 7.0
    
    def test_zero_operand(self):
        """Test operations involving zero."""
        calc = Calculator()
        result = calc.calculate(0, 5, '+')
        assert result == 5


class TestCalculatorInputValidation:
    """Test input validation and error handling."""
    
    def test_invalid_operator(self):
        """Test invalid operator raises ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Invalid Operator"):
            calc.calculate(5, 3, '%')
    
    def test_division_by_zero(self):
        """Test division by zero raises ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.calculate(10, 0, '/')
    
    def test_division_by_zero_float(self):
        """Test division by zero with float raises ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.calculate(5.5, 0.0, '/')
    
    def test_invalid_operator_symbols(self):
        """Test various invalid operators."""
        calc = Calculator()
        invalid_operators = ['&', '^', '!', '=', 'x', 'add']
        for op in invalid_operators:
            with pytest.raises(ValueError, match="Invalid Operator"):
                calc.calculate(5, 3, op)


class TestCalculatorUndo:
    """Test undo functionality."""
    
    def test_single_undo(self):
        """Test undoing a single calculation."""
        calc = Calculator()
        calc.calculate(5, 3, '+')  # Result: 8
        previous = calc.undo()
        assert previous == 0  # Back to initial state
        assert calc.get_result() == 0
    
    def test_undo_multiple_times(self):
        """Test undoing multiple consecutive calculations."""
        calc = Calculator()
        calc.calculate(5, 3, '+')   # Result: 8
        calc.calculate(8, 2, '*')   # Result: 16
        calc.calculate(16, 5, '-')  # Result: 11
        
        assert calc.undo() == 16
        assert calc.undo() == 8
        assert calc.undo() == 0
    
    def test_undo_empty_stack_raises_error(self):
        """Test undo at initial state raises IndexError."""
        calc = Calculator()
        with pytest.raises(IndexError, match="No operations to undo"):
            calc.undo()
    
    def test_undo_after_multiple_calculations(self):
        """Test undo after several calculations."""
        calc = Calculator()
        calc.calculate(10, 5, '+')  # Result: 15
        calc.calculate(15, 3, '*')  # Result: 45
        
        result = calc.undo()
        assert result == 15
        assert calc.get_result() == 15


class TestCalculatorRedo:
    """Test redo functionality."""
    
    def test_single_redo(self):
        """Test redoing a single undone calculation."""
        calc = Calculator()
        calc.calculate(5, 3, '+')   # Result: 8
        calc.undo()                 # Back to 0
        result = calc.redo()        # Back to 8
        assert result == 8
        assert calc.get_result() == 8
    
    def test_redo_multiple_times(self):
        """Test redoing multiple consecutive undos."""
        calc = Calculator()
        calc.calculate(5, 3, '+')   # Result: 8
        calc.calculate(8, 2, '*')   # Result: 16
        calc.calculate(16, 5, '-')  # Result: 11
        
        calc.undo()  # 16
        calc.undo()  # 8
        calc.undo()  # 0
        
        assert calc.redo() == 8
        assert calc.redo() == 16
        assert calc.redo() == 11
    
    def test_redo_empty_stack_raises_error(self):
        """Test redo when redo stack is empty raises IndexError."""
        calc = Calculator()
        with pytest.raises(IndexError, match="Cannot redo when redo stack is empty"):
            calc.redo()
    
    def test_redo_after_calculation_clears_redo_stack(self):
        """Test new calculation clears the redo stack."""
        calc = Calculator()
        calc.calculate(5, 3, '+')   # Result: 8
        calc.undo()                 # Back to 0
        calc.calculate(10, 2, '*')  # Result: 20, clears redo stack
        
        with pytest.raises(IndexError, match="Cannot redo when redo stack is empty"):
            calc.redo()
    
    def test_redo_without_prior_undo(self):
        """Test cannot redo without prior undo."""
        calc = Calculator()
        calc.calculate(5, 5, '+')
        
        with pytest.raises(IndexError, match="Cannot redo when redo stack is empty"):
            calc.redo()