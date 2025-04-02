import ast

def generate_cpp_include():
    cpp_code =  '''#include <iostream>
#include <cmath>
#include <string>
#include <initializer_list>
using namespace std;
\n\n'''
    return cpp_code

def generate_cpp_main():
    cpp_code = "int main(){\n"
    return cpp_code

def get_return_type(node):
    """Determine the C++ return type based on Python function return types."""
    return_types = set()

    for stmt in node.body:
        if isinstance(stmt, ast.Return):
            if isinstance(stmt.value, ast.Constant):
                # Handle constants (integers, strings, etc.)
                return_types.add(type(stmt.value.value).__name__)  # 'int', 'str', etc.
            elif isinstance(stmt.value, ast.List):
                return_types.add('list')
            elif isinstance(stmt.value, ast.Tuple):
                return_types.add('tuple')
            elif isinstance(stmt.value, ast.Name):
                return_types.add('variable')  # A variable could be any type
            # Add additional conditions for more types as needed

    if 'str' in return_types:
        return 'std::string'
    elif 'list' in return_types or 'tuple' in return_types:
        return 'std::vector'  # Assuming vectors for lists/tuples
    elif 'int' in return_types:
        return 'int'
    elif 'float' in return_types:
        return 'double'
    else:
        return 'void'

def generate_function_header(node):
    """Generate C++ function header from a Python function."""
    # return_type = get_return_type(node)
    cpp_code = f"auto {node.name}("
    try:
        args = [f"{arg.annotation.id} "+arg.arg for arg in node.args.args]
    except AttributeError as e:
        print("ERROR:")
        print("    No Support for Dynamic Typed Function Parameters Yet:")
        print("Add Type to Function Parameters:")
        print("    Example: my_func(a:int,b:string)")
        exit()

    cpp_code += ", ".join(args).replace("string","std::string").replace("float","double")
    
    cpp_code += ") {\n"
    return cpp_code


