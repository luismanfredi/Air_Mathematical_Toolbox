import logging
import math

logger = logging.getLogger(__name__)

# Operações
def add(x: float, y: float) -> float:
    return x + y 

def sub(x: float, y: float) -> float:
    return x - y

def mul(x: float, y: float) -> float:
    return x * y

def div(x: float, y: float) -> float:
    if y == 0: # trata divisão por zero
        logger.error("Divisão por zero: %s / %s", x, y)
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def power(x: float, y: float) -> float:
    return x ** y

def sqrt(x: float) -> float:
    if x < 0: # raíz quadrada deve ser positiva para os reais
        logger.error("Tentativa de raíz quadrada de número negativo: %s", x)
        raise ValueError("Square root is only defined for x >= 0 in reals.")
    return math.sqrt(x)

# Aplica operações binárias (Num | op | Num)
def apply_binary(op: str, x: float, y: float) -> float:
    if op == "+":
        result = add(x, y)
        logger.debug("Operação de adição aplicada: %f %s %f = %f", x, op, y, result)
        return result
    if op == "-":
        result = sub(x, y)
        logger.debug("Operação de subtração aplicada: %f %s %f = %f", x, op, y, result)
        return result
    if op == "*":
        result = mul(x, y)
        logger.debug("Operação de multiplicação aplicada: %f %s %f = %f", x, op, y, result)
        return result
    if op == "/":
        result = div(x, y)
        logger.debug("Operação de divisão aplicada: %f %s %f = %f", x, op, y, result)
        return result
    if op == "^":
        result = power(x, y)
        logger.debug("Operação de potência aplicada: %f %s %f = %f", x, op, y, result)
        return result
    logger.warning("Operador binário não reconhecido: %s", op)
    raise ValueError(f"Unknown binary operator: {op}") # caso o operador não exista

# Aplica operações unárias (Num | op)
def apply_unary(name: str, x: float) -> float:
    if name == "sqrt":
        result = sqrt(x)
        logger.debug("Operação aplicada: %s%f = %f", name, x, result)
        return result
    logger.warning("Operador unário não reconhecido: %s", name)
    raise ValueError(f"Unknown unary operator: {name}") # caso o operador não exista