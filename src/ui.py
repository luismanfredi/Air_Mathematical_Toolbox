from typing import Optional, List
import logging

from src.formatting import fmt, separator
from src.parsing import parse_number, parse_op
from src.engine import apply_binary, apply_unary
import src.tokenizer as tokenizer 

logger = logging.getLogger(__name__)

# Imprime ajuda para o usuário
def help_airscal() -> None:
    logger.info("Menu de ajuda a mostra")
    separator()
    print(      
        "Air v0 - Help\n"
        "Commands:\n"
        " q / quit  -> exit\n" 
        " c / clear -> clear\n"
        " h / help  -> show help\n"
        " r / hist  -> show history\n"
        "How does the Air Simple Calculator works?\n"
        "When 'Num:' appears in the terminal you can enter\n"
        "a number within the real set. It's simple!\n"
        "Then, 'Op:' appears and you can enter one of the six operators\n"
        "(+, -, *, /, ^, sqrt).\n"
        "Typing something like '1 + 1' in the 'Num:' input doesn't work."
    )

# Mostra histórico ao usuário em forma de lista, com máximo de 10 operações
def show_history(history: List[str], limit: int = 10) -> None:
    logger.info("Histórico a mostra")
    separator()
    print("History:")
    if not history: # caso histórico esteja vazio
        print("  (empty)")
    else:
        for line in history[-limit:]: 
            print(" ", line)

# Air Simple Calculator
def airscal() -> None:
    logger.info("Calculadora começando...")
    separator()
    print(
        "Welcome to the Air Simple Calculator!\n"
        "This is a simple calculator with the four basic operations, plus square roots and exponentiation.\n"
        "Have fun — and don’t forget to check out the other Air Tools!\n\n"
        "Commands:\n"
        " q / quit  -> exit\n" 
        " c / clear -> clear\n"
        " h / help  -> show help\n"
        " r / hist  -> show history\n"
    )

    # Valor de current_value pode ser um float ou None, começa com None
    current_value: Optional[float] = None

    # Histórico com strings
    history: List[str] = []

    while True:
        
        # Caso seja esteja rodando pela primeira vez, ou clear for usado
        if current_value is None:
            while True:
                # Processo ultilizado nos dois números e na operação
                # associa o valor de kind a um Token e payload ao conteúdo
                # chama a função com o parse do que o usuário deve digitar, nesse caso parse_number
                # ans=None já que essa é a primeira operação
            
                separator()
                kind, payload = parse_number(input("Num: "), ans=None) # associa o valor de kind a um Token e payload ao conteúdo
                if kind == "NUMBER":
                    current_value = float(payload) # current_value = número digitado pelo usuário
                    print(fmt(current_value)) # imprime com formatação
                    break
        
                # Se for um comando
                if kind == "COMMAND": 
                    cmd = str(payload) 
                    if cmd == "QUIT":
                        logger.info("Aplicação encerrada")
                        separator()
                        print("Thank you for using Air Simple Calculator!")
                        return
                    if cmd == "HELP":
                        help_airscal()
                        continue
                    if cmd == "CLEAR": # já estamos sem um valor, apenas volta ao início do loop
                        logger.info("Calcudora limpa")
                        continue
                    if cmd == "HISTORY":
                        show_history(history)
                        continue

                # Input inválido
                separator()
                print("Attention! Enter a real number or a command (h for help).")
 
        # Pedir operação
        while True:
            separator()
            # Mesmo processo de antes, porém com parse_op dessa vez
            kind, payload = parse_op(input("Op: "))
            
            # Se for uma operação
            if kind in ("BINARY_OP", "UNARY_OP"):
                op_kind = kind # token armazenado em op_kind
                op_name = str(payload) # nome armazenado em op_name
                break

            # Se for um comando
            if kind == "COMMAND":
                cmd = str(payload)
                if cmd == "QUIT":
                    logger.info("Aplicação encerrada")
                    separator()
                    print("Thank you for using Air Simple Calculator!")
                    return
                if cmd == "HELP":
                    help_airscal()
                    continue
                if cmd == "CLEAR": 
                    current_value = None
                    break
                if cmd == "HISTORY":
                    show_history(history)
                    continue
            
            # Operador inválido
            separator()
            print("Attention! Invalid Operator. Use h for help.")

        # Se o comando for clear
        if current_value is None:
            continue

        try:
            # Se a operação for unária
            if op_kind == "UNARY_OP":
                print(f"{op_name}{fmt(current_value)}")
                separator()
                before = current_value # armazenamos o valor pois ele será alterado na próxima linha
                current_value = apply_unary(op_name, current_value) # operação aplicada
                line = f"{op_name}({fmt(before)}) = {fmt(current_value)}"
                history.append(line)
                print(line)
                continue

            while True:
                print(f"{fmt(current_value)} {op_name}")
                separator()

                # Pedir o segundo número
                kind, payload = parse_number(input("Num: "), ans=current_value) # ans será o resultado anterior
                if kind == "NUMBER":
                    num2 =  float(payload)
                    break
                
                # Se for um comando
                if kind == "COMMAND":
                    cmd = str(payload)
                    if cmd == "QUIT":
                        logger.info("Aplicação encerrada")
                        separator()
                        print("Thank you for using Air Simple Calculator!")
                        return
                    if cmd == "HELP":
                        help_airscal()
                        continue
                    if cmd == "CLEAR":
                        current_value = None
                        break
                    if cmd == "HISTORY":
                        show_history(history)
                        continue

                # Input inválido
                
                print("Attention! Invalid number. Use h for help.")

            # Se o comando for clear
            if current_value is None:
                logger.info("Calcudora limpa")
                continue
            
            # Execução da operação binária
            before = current_value # armazenamos o valor pois ele será alterado na próxima linha
            current_value = apply_binary(op_name, before, num2) # operação aplicada
            line = f"{fmt(before)} {op_name} {fmt(num2)} = {fmt(current_value)}"
            history.append(line)
            print(line)

        except ZeroDivisionError:
            logger.warning("Erro de divisão por zero")
            print("Attention! Can't divide by zero.")
        
        # Caso erro genérico
        except ValueError as e:
            logger.exception("Erro inesperado na aplicação")
            print(f"Attention! {e}")

def scicalculator():

    while True:
        expr = input("Expr: ")
        result, error = tokenizer.run(expr)

        if error:
            print(error.as_string())  
        else:
            print(result)