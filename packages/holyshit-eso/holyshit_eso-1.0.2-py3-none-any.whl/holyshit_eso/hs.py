import argparse, os
from termcolor import colored
from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter
import json

def main():
    error = colored("[ERROR]", "red")
    info = colored("[INFO]", "green")
    
    #handle args
    parser = argparse.ArgumentParser(description="PyCodeObfuscator Script")
    parser.add_argument("file", metavar="file", type=str, help="Path to the file to be obfuscated")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output, may affect performance on older machines")
    parser.add_argument("-d", "--debug", action="store_true", help="Enables debug output, which prints information about the interpreting process while the script is being executed.")
    args = parser.parse_args()
    file_path = args.file

    #initialize
    lexer = Lexer(file_path, args.verbose)
    parser = Parser(args.verbose)
    interpreter = Interpreter(args.verbose, args.debug)
        
    #load and tokenize script
    lexer.load_file()
    tokens = lexer.lexer()
    if tokens is None:
        print(error, "Failed to tokenize script.")
        return

    #parse the tokens (for easier execution)
    ast = parser.parser(tokens)
    if ast is None:
        print(error, "Failed to parse tokens.")
        return

    #run the code (item by item)
    interpreter.interpreter(ast)


