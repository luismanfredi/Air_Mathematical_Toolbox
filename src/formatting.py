import logging

logger = logging.getLogger(__name__)
    
def fmt(n: float, decimals: int = 10) -> str:
    if abs(n) < 1e-12: # número muito pequeno = 0
        n = 0.0

    n = round(n, decimals) # arredonda em 10 casas decimais

    if float(n).is_integer(): # se for do tipo 1.0 (casa decimais com 0 apenas) 
        return str(int(n)) # retorna str agora do tipo 1, em int
    
    s = f"{n:.{decimals}f}".rstrip("0").rstrip(".") # formata decimais, e tira zeros a direita da vírgula.
    
    logger.debug("Número formatado: %s", s)
    return s

def separator():
    print("-" * 40)