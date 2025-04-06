import os
from termcolor import colored

class CircularCounter:
    def __init__(self):
        self.value = 0
        self.max_value = 256

    def increment(self):
        self.value = (self.value + 1) % (self.max_value + 1)
        if self.value == 0:
            self.value = self.max_value

    def decrement(self):
        self.value = (self.value - 1) % (self.max_value + 1)
        if self.value == self.max_value:
            self.value = self.max_value

    def get_value(self):
        return self.value


class Interpreter:
    def __init__(self, verbose: bool, debug: bool):
        self.error = colored("[ERROR]", "red")
        self.info = colored("[INFO]", "green")
        self.verbose = verbose
        self.terminate = False
        self.debug = debug

        # Global variables stored in __init__
        self.mode = 0  # 1 = cursor, 2 = cell
        self.cursor_pos = CircularCounter()
        self.cursor_value = CircularCounter()
        self.cell_strip = [0] * 1025

    def interpreter(self, ast, clear_screen=True):
        # Clear the screen only if clear_screen is True
        if clear_screen:
            if os.name == 'nt':  # Windows
                os.system("cls")
            else:  # macOS/Linux/Unix
                os.system("clear")

        i = 0

        while i < len(ast):
            if clear_screen:
                if self.debug:
                    print(self.info, f"Processing instruction: {ast[i]['type']}")

            if self.terminate:  # Stop execution if an error has been encountered
                print(self.error, "Execution halted due to an error.")
                break

            item = ast[i]

            match item["type"]:
                case "COMMENT":
                    pass

                case "MODE_CURSOR":
                    if self.mode == 1:
                        print(self.error, "There was an error during interpreting: Tried to enter cursor mode while already in cursor mode.")
                        self.terminate = True
                        return
                    else:
                        self.mode = 1

                case "MODE_CELL":
                    if self.mode == 2:
                        print(self.error, "There was an error during interpreting: Tried to enter cell mode while already in cell mode.")
                        self.terminate = True
                        return
                    else:
                        self.mode = 2

                case "MOVE_RIGHT":
                    if self.mode == 1:
                        self.cursor_pos.increment()
                    else:
                        print(self.error, "There was an error during interpreting: Can't move cursor when not in cursor mode.")
                        self.terminate = True
                        return

                case "MOVE_LEFT":
                    if self.mode == 1:
                        self.cursor_pos.decrement()
                    else:
                        print(self.error, "There was an error during interpreting: Can't move cursor when not in cursor mode.")
                        self.terminate = True
                        return

                case "INCREMENT":
                    if self.mode == 1:
                        self.cursor_value.increment()
                    else:
                        print(self.error, f"There was an error during interpreting: Can't change cursor value when not in cursor mode. MODE: {self.mode}")
                        self.terminate = True
                        return

                case "DECREMENT":
                    if self.mode == 1:
                        self.cursor_value.decrement()
                    else:
                        print(self.error, "There was an error during interpreting: Can't change cursor value when not in cursor mode.")
                        self.terminate = True
                        return

                case "RESET_CURSOR":
                    if self.mode == 1:
                        self.cursor_value.value = 0
                    else:
                        print(self.error, "There was an error during interpreting: Can't reset cursor value when not in cursor mode.")
                        self.terminate = True
                        return

                case "STORE":
                    if self.mode == 2:
                        self.cell_strip[self.cursor_pos.value] = self.cursor_value.get_value()  # Store cursor value in the current cell
                    else:
                        print(self.error, "Can't modify a cell's value when not in cell mode.")
                        self.terminate = True
                        return

                case "LOOP":
                    loop_condition = int(item["loop_condition"]) if isinstance(item["loop_condition"], str) else item["loop_condition"]
                    if item["value"] is None:
                        print(self.error, "There was an error during interpreting: Missing loop body.") 
                        self.terminate = True
                        return
                    while self.cell_strip[self.cursor_pos.value] != loop_condition:
                        self.interpreter(item["value"], clear_screen=False)
                        if self.terminate:
                            return

                case "IF_STATEMENT":
                    if_condition = int(item["if_statement_condition"]) if isinstance(item["if_statement_condition"], str) else item["if_statement_condition"]
                    if item["value"] is None:
                        print(self.error, f"There was an error during interpreting: Missing body for IF statement with condition: {if_condition}.")
                        self.terminate = True
                        return
                    if self.cell_strip[self.cursor_pos.value] == if_condition:
                        while True:
                            self.interpreter(item["value"], clear_screen=False)
                            if self.terminate:
                                return
                            break


                case "PRINT":
                    if self.mode == 2:
                        print(chr(self.cell_strip[self.cursor_pos.value]), end="")
                    else:
                        print(self.error, "Can't print a cell's value when not in cell mode.")
                        self.terminate = True
                        return

                case "INPUT":
                    if self.mode == 1:
                        input_value = input()
                        if input_value == "":
                            self.cursor_value.value = 0
                            i += 1
                            continue
                        if len(input_value) == 1:  
                            self.cursor_value.value = ord(input_value)
                        else:
                            print(self.error, "Input value is too long (maximum of 1 character).")
                            self.terminate = True
                            return
                    else:
                        print(self.error, "Cant Take in an input when not in cursor mode.")
                        self.terminate = True
                        return
                        

            i += 1
