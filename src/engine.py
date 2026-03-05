import math

# Operações
def add(x: float, y: float) -> float:
    return x + y 

def sub(x: float, y: float) -> float:
    return x - y

def mul(x: float, y: float) -> float:
    return x * y

def div(x: float, y: float) -> float:
    if y == 0: # divisão por zero
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def power(x: float, y: float) -> float:
    return x ** y

def sqrt(x: float) -> float:
    if x < 0: # raíz quadrada deve ser positiva para os reais
        raise ValueError("Square root is only defined for x >= 0 in reals.")
    return math.sqrt(x)

# Aplica operações binárias (Num | op | Num)
def apply_binary(op: str, x: float, y: float) -> float:
    if op == "+":
        return add(x, y)
    if op == "-":
        return sub(x, y)
    if op == "*":
        return mul(x, y)
    if op == "/":
        return div(x, y)
    if op == "^":
        return pow(x, y)
    raise ValueError(f"Unknown binary operator: {op}") # caso o operador não exista

# Aplica operações unárias (Num | op)
def apply_unary(name: str, x: float) -> float:
    if name == "sqrt":
        return sqrt(x)
    raise ValueError(f"Unknown unary operator: {name}") # caso o operador não exista

