from src.formatting import fmt

TT_NUMBER = "NUMBER"
TT_OPERATOR = "OPERATOR"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"
TT_FUNCTION = "FUNCTION"
TT_CONSTANT = "CONSTANT"

CONSTANTS = {"e", "pi"}
BINARY_OPS = {"+", "-", "*", "/"} 
DIGITS = "0123456789"
FUNCTIONS = {"funcção"}

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f"{self.type}:{self.value}"
        return f"{self.type}"
    
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        return f"{self.error_name}: {self.details}"
    
class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__("Illegal Character", details)   
         
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def make_tokens(self):
        tokens = []
        
        while self.current_char != None:
            if self.current_char == " ":
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(Token(TT_NUMBER))
                self.advance()
            elif self.current_char in BINARY_OPS:
                tokens.append(Token(TT_OPERATOR))
                self.advance()
            elif self.current_char in CONSTANTS:
                tokens.append(Token(TT_CONSTANT))
                self.advance()
            elif self.current_char in FUNCTIONS:
                tokens.append(Token(TT_FUNCTION))
                self.advance()
            elif self.current_char == "(":
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ""
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + ".":
            if self.current_char == ".":
                if dot_count == 1:
                    print("Dois pontos no mesmo num")
                    break
                dot_count += 1
                num_str += "."
            else:
                num_str += self.current_char
            self.advance()

        return Token(TT_NUMBER, float(num_str))

    
def run(expr):
    lexer = Lexer(expr)
    tokens, error = lexer.make_tokens()

    return tokens, error