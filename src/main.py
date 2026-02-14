from src.calculator import Calculator


def display_menu():
    """Display the calculator menu options."""
    print("\n" + "="*50)
    print("CALCULATOR WITH UNDO/REDO")
    print("="*50)
    print("Operations: +, -, *, /")
    print("Commands: undo, redo, clear, exit")
    print("="*50)


def display_result(result):
    """Display the current result."""
    print(f"Result: {result}")


def main():
    """Main calculator loop."""
    calc = Calculator()
    
    print("Welcome to Calculator with Undo/Redo!")
    print("Type 'help' for commands")
    
    while True:
        display_menu()
        print(f"Current Result: {calc.get_result()}")
        
        user_input = input("\nEnter command (help/exit): ").strip().lower()
        
        # Handle special commands
        if user_input == 'exit':
            print("Goodbye!")
            break
        
        elif user_input == 'help':
            print("\nCommands:")
            print("  calc <num1> <operator> <num2>  - Perform calculation")
            print("  undo                           - Undo last operation")
            print("  redo                           - Redo last undone operation")
            print("  clear                          - Reset calculator to 0")
            print("  exit                           - Exit calculator")
            continue
        
        elif user_input == 'undo':
            try:
                result = calc.undo()
                display_result(result)
            except IndexError as e:
                print(f"Error: {e}")
        
        elif user_input == 'redo':
            try:
                result = calc.redo()
                display_result(result)
            except IndexError as e:
                print(f"Error: {e}")
        
        elif user_input == 'clear':
            calc = Calculator()
            print("Calculator reset to 0")
        
        elif user_input.startswith('calc '):
            try:
                # Parse input: "calc 5 + 3"
                parts = user_input[5:].split()
                
                if len(parts) < 3:
                    print("Error: Please use format 'calc <num1> <operator> <num2>'")
                    continue
                
                try:
                    value1 = float(parts[0])
                except ValueError:
                    print(f"Error: '{parts[0]}' is not a valid number")
                    continue
                
                operator = parts[1]
                
                try:
                    value2 = float(parts[2])
                except ValueError:
                    print(f"Error: '{parts[2]}' is not a valid number")
                    continue
                
                result = calc.calculate(value1, value2, operator)
                display_result(result)
            
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
        
        else:
            print("Invalid command. Type 'help' for available commands.")


if __name__ == "__main__":
    main()