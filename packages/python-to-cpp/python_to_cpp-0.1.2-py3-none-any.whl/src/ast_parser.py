import ast

def parse_python_code(python_code):
    """Parse Python code into an Abstract Syntax Tree."""
    try:
        tree = ast.parse(python_code)
        return tree
    except SyntaxError as e:
        print(f"Syntax error: {e}")
        return None
