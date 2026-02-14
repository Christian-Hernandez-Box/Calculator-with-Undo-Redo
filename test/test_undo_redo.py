import pytest
from src.calculator import Calculator


class TestUndoRedoEdgeCases:
    """Test edge cases and boundary conditions for undo/redo."""
    
    def test_undo_redo_with_zero_result(self):
        """Test undo/redo when result is zero."""
        calc = Calculator()
        calc.calculate(5, 5, '-')   # Result: 0
        calc.undo()                 # Back to 0 (initial)
        calc.redo()                 # Back to 0
        assert calc.get_result() == 0
    
    def test_undo_redo_with_negative_result(self):
        """Test undo/redo with negative results."""
        calc = Calculator()
        calc.calculate(3, 10, '-')  # Result: -7
        calc.undo()
        assert calc.get_result() == 0
        calc.redo()
        assert calc.get_result() == -7
    
    def test_undo_redo_with_decimal_result(self):
        """Test undo/redo with decimal results."""
        calc = Calculator()
        calc.calculate(7, 2, '/')   # Result: 3.5
        calc.undo()
        assert calc.get_result() == 0
        calc.redo()
        assert calc.get_result() == 3.5
    
    def test_multiple_undos_then_new_calculation(self):
        """Test new calculation after multiple undos clears redo."""
        calc = Calculator()
        calc.calculate(10, 5, '+')  # Result: 15
        calc.calculate(15, 2, '*')  # Result: 30
        calc.calculate(30, 10, '-') # Result: 20
        
        calc.undo()
        calc.undo()
        # Redo stack should have 2 items
        calc.calculate(5, 5, '+')   # New calculation
        
        with pytest.raises(IndexError):
            calc.redo()
    
    def test_undo_redo_state_consistency(self):
        """Test that undo/redo maintains consistent state."""
        calc = Calculator()
        calc.calculate(100, 5, '/')  # Result: 20
        
        for _ in range(3):
            calc.undo()
            calc.redo()
        
        assert calc.get_result() == 20
    
    def test_redo_empty_after_new_calculation(self):
        """Test redo stack is empty after new calculation."""
        calc = Calculator()
        calc.calculate(5, 3, '+')
        calc.undo()
        calc.calculate(10, 2, '*')
        
        # Verify redo is empty
        with pytest.raises(IndexError, match="Cannot redo"):
            calc.redo()
    
    def test_undo_beyond_initial_state(self):
        """Test cannot undo beyond initial state."""
        calc = Calculator()
        calc.calculate(5, 5, '+')
        calc.undo()
        
        # Should raise on second undo
        with pytest.raises(IndexError, match="No operations to undo"):
            calc.undo()
    
    def test_complex_workflow(self):
        """Test realistic workflow with mixed operations."""
        calc = Calculator()
        
        # Do calculations
        calc.calculate(10, 5, '+')   # 15
        assert calc.get_result() == 15
        
        calc.calculate(15, 2, '*')   # 30
        assert calc.get_result() == 30
        
        # Undo back
        calc.undo()
        assert calc.get_result() == 15
        
        # Redo forward
        calc.redo()
        assert calc.get_result() == 30
        
        # New calculation clears redo
        calc.calculate(30, 6, '/')   # 5
        assert calc.get_result() == 5
        
        # Undos should work
        calc.undo()
        assert calc.get_result() == 30
        
        calc.undo()
        assert calc.get_result() == 15
    
    def test_undo_redo_with_large_numbers(self):
        """Test undo/redo with large numbers."""
        calc = Calculator()
        calc.calculate(1000000, 2000000, '+')  # 3000000
        calc.undo()
        calc.redo()
        assert calc.get_result() == 3000000
    
    def test_undo_redo_with_very_small_decimals(self):
        """Test undo/redo with very small decimal numbers."""
        calc = Calculator()
        calc.calculate(0.0001, 0.0002, '+')  # 0.0003
        calc.undo()
        calc.redo()
        assert abs(calc.get_result() - 0.0003) < 1e-10
    
    def test_alternate_undo_redo(self):
        """Test alternating undo and redo operations."""
        calc = Calculator()
        calc.calculate(2, 3, '+')   # Result: 5
        
        calc.undo()      # 0
        calc.redo()      # 5
        calc.undo()      # 0
        calc.redo()      # 5
        
        assert calc.get_result() == 5
    
    def test_long_calculation_chain(self):
        """Test long sequence of calculations with undo/redo."""
        calc = Calculator()
        for i in range(1, 6):
            calc.calculate(i, 1, '+')
        
        # Undo all
        for _ in range(5):
            calc.undo()
        
        # Redo all
        for _ in range(5):
            calc.redo()
        
        assert calc.get_result() == 6  # 5 + 1
    
    def test_undo_after_undo_redo_sequence(self):
        """Test undo after a complex undo/redo sequence."""
        calc = Calculator()
        calc.calculate(10, 2, '+')   # 12
        calc.calculate(12, 3, '*')   # 36
        
        calc.undo()      # 12
        calc.redo()      # 36
        calc.undo()      # 12
        
        assert calc.get_result() == 12
    
    def test_multiple_redo_clears_on_new_calc(self):
        """Test multiple redos become unavailable after new calculation."""
        calc = Calculator()
        calc.calculate(5, 2, '+')    # 7
        calc.calculate(7, 3, '*')    # 21
        calc.calculate(21, 7, '/')   # 3
        
        # Undo all three
        calc.undo()  # 21
        calc.undo()  # 7
        calc.undo()  # 0
        
        # Redo two
        calc.redo()  # 7
        calc.redo()  # 21
        
        # New calculation clears remaining redo
        calc.calculate(21, 3, '-')   # 18
        
        with pytest.raises(IndexError):
            calc.redo()
    
    def test_arithmetic_chain_with_undo_redo(self):
        """Test realistic arithmetic chain with undo/redo."""
        calc = Calculator()
        
        # Build: ((2 + 3) * 4) - 5 = 15
        calc.calculate(2, 3, '+')    # 5
        calc.calculate(5, 4, '*')    # 20
        calc.calculate(20, 5, '-')   # 15
        
        assert calc.get_result() == 15
        
        # Undo last operation
        calc.undo()
        assert calc.get_result() == 20
        
        # Redo it
        calc.redo()
        assert calc.get_result() == 15