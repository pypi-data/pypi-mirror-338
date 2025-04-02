import sys
import ast
from .ast_parser import parse_python_code
from .ast_to_cpp_converter import convert_ast_to_cpp, get_func_code
from .codegen import generate_cpp_include, generate_cpp_main
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python transpiler.py <python_file.py>")
        sys.exit(1)

    path = os.getcwd() 
    python_file = path +"\\"+ sys.argv[1]
    
    # Read Python source code
    with open(python_file, 'r') as f:
        python_code = f.read()
    
    # Parse the Python code
    parsed_ast = parse_python_code(python_code)
    
    if parsed_ast is None:
        print("Failed to parse Python code.")
        sys.exit(1)
    
    # Convert the AST to C++ code
    cpp_code = ""
    global_code = generate_cpp_include()


    for node in parsed_ast.body:
        # print(ast.dump(node))
        cpp_code += convert_ast_to_cpp(node)
        
    

    cpp_code = global_code + get_func_code() + generate_cpp_main() + cpp_code + "return 0;\n}\n"    
    
    # Save the C++ code to a .cpp file
    cpp_file = python_file.replace(".py", ".cpp")
    with open(cpp_file, 'w') as f:
        f.write(cpp_code)
    
    print(f"Generated C++ code saved to {cpp_file}")

if __name__ == "__main__":
    main()
