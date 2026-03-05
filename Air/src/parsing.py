from __future__ import annotations
from typing import Tuple, Union, Optional

# Comando globais
COMMANDS = {
    "q": "QUIT",
    "quit": "QUIT",
    "h": "HELP",
    "help": "HELP",
    "c": "CLEAR",
    "clear": "CLEAR",
    "r": "HISTORY",
    "hist": "HISTORY",
    "history": "HISTORY",
}

# Operações do tipo Num | Op | Num
BINARY_OPS = {"+", "-", "*", "/", "^"}

# Operações do tipo Num | Op 
UNARY_OPS = {"sqrt", "√"}

# Token do tipo "NUMBER"; "COMMAND" e etc. 
# Informando qual o tipo de informação o usuário digitou
Kind = str

# Conteúdo real do que o usuário digitou
Payload = Union[float, str] # pode ser float ou str

# Apelido de type, documentação
ParseResult = Tuple[Kind, Payload]

# Retorna input do usuário em lower e sem espaços deixados sem querer
def _normalize(s: str) -> str:
    return s.strip().lower()

# Analisa comandos
def parse_commands(s: str) -> Optional[ParseResult]:
    s = _normalize(s)

    if s in COMMANDS: # se é um comando...
        return("COMMAND", COMMANDS[s]) # retorna token para tomada de decisão, e o conteúdo (como "QUIT")
    return None

# Analisa números
def parse_number(s: str, ans: Optional[float] = None) -> ParseResult:
    s = _normalize(s)

    # caso o usuário digite um comando...
    cmd = parse_commands(s) 
    if cmd is not None: # se for um comando retorna o comando
        return cmd
    
    # para usar a última resposta
    if s == "ans":
        if ans is None: # se não tiver resultado anterior
            return ("INVALID, ANS_NOT_SET")
        return ("NUMBER", float(ans)) # se tiver resultado anterior
    
    # retorna o token e o número em float, caso seja um número
    try:
        return ("NUMBER", float(s))
    except ValueError:
        return ("INVALID", "NOT_A_NUMBER")
    
# Analisa operações
def parse_op(s: str) -> ParseResult:
    s = _normalize(s)

    # caso o usuário digite um comando...
    cmd = parse_commands(s)
    if cmd is not None: # se for um comando retorna o comando
        return cmd
    
    # retorna o tipo de operação e a operação
    if s in BINARY_OPS:
        return ("BINARY_OP", s)
    if s in UNARY_OPS:
        return ("UNARY_OP", "sqrt")
    
    return ("INVALID", "NOT_AN_OPERATOR") # caso operador inválido