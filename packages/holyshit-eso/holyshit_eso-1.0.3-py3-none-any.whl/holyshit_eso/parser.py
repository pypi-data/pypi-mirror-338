from termcolor import colored
import json

class Parser:
    def __init__(self, verbose):
        self.error = colored("[ERROR]", "red")
        self.info = colored("[INFO]", "green")
        self.verbose = verbose

    
    def parser(self, tokens: list):
        ast = []  # Abstract Syntax Tree
        i = 0
    
        while i < len(tokens):
            token = tokens[i]
    
            # Handle Loop Syntax
            if token["type"] == "LOOP_COND":
                loop_condition = token["value"][1:]  # Extract condition
                i += 1  # Move to next token
                if i < len(tokens) and tokens[i]["type"] == "LOOP_START":
                    i += 1
                    new_loop = {"type": "LOOP", "loop_condition": loop_condition, "value": []}
                    loop_content = []
                    while i < len(tokens) and tokens[i]["type"] != "LOOP_END":
                        loop_content.append(tokens[i])
                        i += 1
                    if i >= len(tokens):  # Missing LOOP_END
                        print(self.error, f"Missing LOOP_END for loop starting at: \"{token['value']}\"")
                        return None
                    new_loop["value"] = self.parser(loop_content)  # Recursively parse loop content
                    ast.append(new_loop)
    
            # Handle If Syntax
            elif token["type"] == "IF_COND":
                if_condition = token["value"][1:]  # Extract condition
                i += 1  # Move to IF_START
                if i < len(tokens) and tokens[i]["type"] == "IF_START":
                    i += 1
                    new_if_statement = {"type": "IF_STATEMENT", "if_statement_condition": if_condition, "value": []}
                    if_statement_content = []
                    while i < len(tokens) and tokens[i]["type"] != "IF_END":
                        if_statement_content.append(tokens[i])
                        i += 1
                    if i >= len(tokens):  # Missing IF_END
                        print(self.error, f"Missing IF_END for if statement starting at: \"{token['value']}\"")
                        return None
                    new_if_statement["value"] = self.parser(if_statement_content)  # Recursively parse if content
                    ast.append(new_if_statement)
                else:
                    print(self.error, f"Missing IF_START for if condition: \"{if_condition}\"")
                    return None
    
            # Fallback for other tokens
            else:
                ast.append(token)
    
            i += 1
    
        return ast
