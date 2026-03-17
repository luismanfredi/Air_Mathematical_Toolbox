from __future__ import annotations
from typing import Tuple, Union, Optional

import logging

logger = logging.getLogger(__name__)

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
def parse_command(s: str) -> Optional[ParseResult]:
    s = _normalize(s)

    if s in COMMANDS: # se é um comando...
        logger.info("Comando reconhecido: %s", s)
        return ("COMMAND", COMMANDS[s]) # retorna token para tomada de decisão, e o conteúdo (como "QUIT")
    return None

# Analisa números
def parse_number(s: str, ans: Optional[float] = None) -> ParseResult:
    logger.debug("Input recebido: %s", s)
    s = _normalize(s)

    # caso o usuário digite um comando...
    cmd = parse_command(s) 
    if cmd is not None: # se for um comando retorna o comando
        return cmd
    
    # para usar a última resposta
    if s == "ans":
        if ans is None: # se não tiver resultado anterior
            return ("INVALID", "ANS_NOT_SET")
        return ("NUMBER", float(ans)) # se tiver resultado anterior
    
    # retorna o token e o número em float, caso seja um número
    try:
        str_to_float = ("NUMBER", float(s))
        logger.debug("Input transformado em número: %s", s)
        return str_to_float
    except ValueError:
        logger.warning("Input inválido: %s", s)
        return ("INVALID", "NOT_A_NUMBER")
    
# Analisa operações
def parse_op(s: str) -> ParseResult:
    s = _normalize(s)

    # caso o usuário digite um comando...
    cmd = parse_command(s)
    if cmd is not None: # se for um comando retorna o comando
        return cmd
    
    # retorna o tipo de operação e a operação
    if s in BINARY_OPS:
        logger.info("Comando binário recebido: %s", s)
        return ("BINARY_OP", s)
    if s in UNARY_OPS:
        logger.info("Comando unário recebido: %s", s)
        return ("UNARY_OP", "sqrt")
    
    logger.warning("Input Inválido: %s", s)
    return ("INVALID", "NOT_AN_OPERATOR") # caso operador inválido