from __future__ import annotations

script = str.maketrans("0123456789-.", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻·" ) # unicode para potências e raízes

# Formatações

# Transforma números em índices
def translate(n):
    return str(n).translate(script)

# Transforma números em índices
def format_index(i) -> str:
    if i == 2: 
        return "√" # símbolo padrão de raíz quadrada
    else:
        return f"{translate(i)}√" # impressão com índice formatado
    
def fmt(n: float, decimals: int = 10):
    if abs(n) < 1e-12: # número muito pequeno = 0
        n = 0.0

    n = round(n, decimals) # arredonda em 10 casas decimais

    if float(n).is_integer(): # se for do tipo 1.0 (casa decimais com 0 apenas) 
        return str(int(n)) # retorna str agora do tipo 1, em int
    
    s = f"{n:.{decimals}f}".rstrip("0").rstrip(".") # formata decimais, e tira zeros a direita da vírgula.
    return s