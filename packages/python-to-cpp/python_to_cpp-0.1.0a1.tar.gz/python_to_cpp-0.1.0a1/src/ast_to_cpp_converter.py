import ast
from .codegen import generate_function_header

func_code = ""
var_list = []

def get_func_code():
    return func_code

def convert_ast_to_cpp(node,printing=False):

    global func_code,var_list
    """Recursively convert Python AST nodes to C++ code."""
    cpp_code = ""
    

    if isinstance(node, ast.FunctionDef):
        func_code += generate_function_header(node)
        
        for stmt in node.body:
            func_code += convert_ast_to_cpp(stmt)
        
        func_code += "}\n"

    elif isinstance(node, ast.Return):
        if isinstance(node.value, ast.Constant):
            return_value = node.value.value
            if isinstance(return_value,str): return_value = f'"{return_value}"'
            cpp_code += f"return {return_value};\n"
        elif isinstance(node.value, ast.Name):
            cpp_code += f"return {node.value.id};\n"
        
    elif isinstance(node, ast.Expr):
        print(ast.dump(node))
        cpp_code += convert_ast_to_cpp(node.value)
        
    elif isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name) and node.func.id == 'print':
            cpp_code += generate_print_statement(node)
        elif isinstance(node.func, ast.Name) and node.func.id == 'str':
            cpp_code += f"to_string({convert_ast_to_cpp(node.args[0])})"
        elif isinstance(node.func, ast.Name) and (node.func.id == 'int' or node.func.id == 'float'):
            if node.func.id == 'int': cpp_code += f"std::stoi({convert_ast_to_cpp(node.args[0])})"
            elif node.func.id == 'float': cpp_code += f"std::stof({convert_ast_to_cpp(node.args[0])})"
        # elif isinstance(node.func, ast.Name) and node.func.id == 'range':
        #     pass

        else:
            args = []
            for arg in node.args:
                if isinstance(arg, ast.Constant):
                    args.append(str(arg.value))
                elif isinstance(arg, ast.Name):
                    args.append(arg.id)
            cpp_code += node.func.id + f"({','.join(args)});\n"
            if printing == True: cpp_code = cpp_code[:-2]
        
    elif isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Pow):
            cpp_code += f"pow({convert_ast_to_cpp(node.left)},{convert_ast_to_cpp(node.right)})"
        elif isinstance(node.op, ast.FloorDiv):
            cpp_code += f"floor({convert_ast_to_cpp(node.left)} {convert_ast_to_cpp(node.op)} {convert_ast_to_cpp(node.right)})"
        else:
            cpp_code += f"{convert_ast_to_cpp(node.left)} {convert_ast_to_cpp(node.op)} {convert_ast_to_cpp(node.right)}"
        
    elif isinstance(node, ast.Constant):
        # Handle constants (strings, numbers, booleans)
        if isinstance(node.value, str):
            cpp_code += f'"{node.value}"'  # String literal
        elif isinstance(node.value, bool):
            cpp_code += "true" if node.value else "false"  # Boolean literal
        elif isinstance(node.value, (int, float)):
            cpp_code += str(node.value)  # Integer or float literal
        else:
            cpp_code += str(node.value)

    elif isinstance(node, ast.Assign):
        targets = node.targets[0]
        if isinstance(targets, ast.Name):
            var_type = ""
            if not targets.id in var_list: var_type = "auto "
            cpp_code += f"{var_type}{targets.id} = {convert_ast_to_cpp(node.value)};\n"
            var_list.append(targets.id)
        elif isinstance(targets, ast.Tuple):
            names = targets.elts
            values = node.value.elts
            for name, value in zip(names,values):
                var_type = ""
                if not name.id in var_list: var_type = "auto "
                cpp_code += f"{var_type}{name.id} = {convert_ast_to_cpp(value)};\n"
                var_list.append(name.id)

    elif isinstance(node, ast.Name):
        cpp_code += node.id

    elif isinstance(node, ast.UnaryOp):
        # Handle unary operations (like -x, not x)
        if isinstance(node.op, ast.USub):
            cpp_code += f"-{convert_ast_to_cpp(node.operand)}"

    # Handle the binary operators in a single elif block
    elif isinstance(node, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow, ast.LShift, ast.RShift, ast.BitAnd, ast.BitOr, ast.BitXor, ast.FloorDiv, ast.MatMult)):
        # Map Python AST operators to C++ equivalents
        operator_map = {
            ast.Add: "+",
            ast.Sub: "-",
            ast.Mult: "*",
            ast.Div: "/",
            ast.Mod: "%",
            ast.Pow: "**",  # In Python, '**' is for power operation. In C++, use 'pow()' from <cmath>.
            ast.LShift: "<<",
            ast.RShift: ">>",
            ast.BitAnd: "&",
            ast.BitOr: "|",
            ast.BitXor: "^",
            ast.FloorDiv: "/",  # In Python, '//' is floor division, in C++ use floor() from <cmath> if necessary
            ast.MatMult: "@",  # Matrix multiplication in Python uses `@`, you might want to handle it specifically for C++ libraries
        }
        cpp_code = operator_map[type(node)]  # Retrieve the operator as string from map

    elif isinstance(node, ast.Subscript):
        # cpp_code += 
        pass

    elif isinstance(node, ast.List):
        # print(ast.dump(node))
        cpp_code += f"{{{','.join([convert_ast_to_cpp(const) for const in node.elts]) }}}"

    elif isinstance(node, ast.For):
        if isinstance(node.iter, ast.Call):
            i = convert_ast_to_cpp(node.target); v = [convert_ast_to_cpp(const) for const in node.iter.args]
            if len(v) == 2: v.append(1)
            cpp_code += f"for (auto {i} = {v[0]}; {i} <= {v[1]}; {i}={i}+{v[2]})"+"{\n"
        else: 
            cpp_code += f"for (auto {convert_ast_to_cpp(node.target)} : {convert_ast_to_cpp(node.iter)})"+"{\n"
        cpp_code += "".join([convert_ast_to_cpp(expr) for expr in node.body]) + "}\n"
        pass

    elif isinstance(node, ast.While):
        pass

    return cpp_code

def generate_print_statement(node):
    """Generate C++ print statement from a Python print function."""
    cpp_code = 'std::cout << '

    for i, arg in enumerate(node.args):
        # Recursively handle each argument of the print function
        cpp_code += convert_ast_to_cpp(arg,printing=True)

        # Add separator for multiple arguments (adding space between them)
        if i < len(node.args) - 1:
            cpp_code += " << ' ' << "

    cpp_code += " << std::endl;\n"
    return cpp_code