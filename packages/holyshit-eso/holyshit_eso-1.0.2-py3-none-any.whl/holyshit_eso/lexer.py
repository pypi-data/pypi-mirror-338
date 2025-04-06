import sys, re
from termcolor import colored

class Lexer():
    def __init__(self, file_path, verbose: bool):
        self.error = colored("[ERROR]", "red")
        self.info = colored("[INFO]", "green")

        self.token_specs = [
            ("COMMENT", r"/.*"),
            ("MODE_CURSOR", r"c"),
            ("MODE_CELL", r"s"),
            ("MOVE_RIGHT", r">"),
            ("MOVE_LEFT", r"<"),
            ("INCREMENT", r"\?"),
            ("RESET_CURSOR", r"r"),
            ("DECREMENT", r"!"),
            ("STORE", r"%"),
            ("LOOP_COND", r"~\d+"),
            ("LOOP_START", r"\["),
            ("LOOP_END", r"\]"),
            ("IF_COND", r"-\d+"),
            ("IF_START", r"\("),
            ("IF_END", r"\)"),
            ("PRINT", r"@"),
            ("INPUT", r"#"),
        ]
    
        self.file_path = file_path
        self.content = self.load_file()
        self.verbose = verbose



    def load_file(self):
        
        if not self.file_path.strip().replace("\ ", "").replace("/", "").endswith(".crap"):
            print(self.error, "File format is unsupported, must be a .crap file.")
            return None
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(self.error, f"Error: File '{self.file_path}' not found.")
            sys.exit(1)
        except Exception as e:
            print(self.error, f"An error occurred: {e}")
            sys.exit(1)
    
    def lexer(self):

        token_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in self.token_specs)
        token_re = re.compile(token_regex)
        tokens = []
        
        for match in token_re.finditer(self.content):

            kind = match.lastgroup
            value = match.group()

            if kind != "WHITESPACE":
                tokens.append({"type": kind, "value": value})
        return tokens