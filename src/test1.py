# src/ui.py
from __future__ import annotations
from typing import Optional, List, Tuple

from .parsing import parse_number, parse_op
from .engine import apply_binary, apply_unary
from .formatting import fmt


def show_help() -> None:
    print("-" * 40)
    print("Air v0 - Help")
    print("Commands:")
    print("  q / quit   -> exit")
    print("  c / clear  -> clear current value")
    print("  h / help   -> show help")
    print("  r / hist   -> show history")
    print("")
    print("Examples:")
    print("  Num: 10")
    print("  Op : +")
    print("  Num: 5")
    print("  Op : sqrt   (applies to current value)")
    print("  Num: pi")
    print("  Num: ans")
    print("-" * 40)


def show_history(history: List[str], limit: int = 10) -> None:
    print("-" * 40)
    print("History:")
    if not history:
        print("  (empty)")
    else:
        for line in history[-limit:]:
            print(" ", line)
    print("-" * 40)


def run() -> None:
    print("-" * 40)
    print("Welcome to Air Simple Calculator")
    print("Commands: q quit | c clear | h help | r hist")
    print("-" * 40)

    current_value: Optional[float] = None
    history: List[str] = []

    while True:
        # 1) pegar número inicial se não tiver current_value
        if current_value is None:
            while True:
                kind, payload = parse_number(input("Num: "), ans=None)
                if kind == "NUMBER":
                    current_value = float(payload)
                    print(fmt(current_value))
                    break

                if kind == "COMMAND":
                    cmd = str(payload)
                    if cmd == "QUIT":
                        print("-" * 40)
                        print("Thank you for using Air!")
                        return
                    if cmd == "HELP":
                        show_help()
                        continue
                    if cmd == "CLEAR":
                        # já está None, só repete
                        continue
                    if cmd == "HISTORY":
                        show_history(history)
                        continue

                # INVALID
                print("-" * 40)
                print("Attention! Enter a real number (or pi/e/ans) or a command (h for help).")
                print("-" * 40)

        # 2) pedir operador
        while True:
            kind, payload = parse_op(input("Op: "))
            if kind in ("BINARY_OP", "UNARY_OP"):
                op_kind = kind
                op_name = str(payload)
                break

            if kind == "COMMAND":
                cmd = str(payload)
                if cmd == "QUIT":
                    print("-" * 40)
                    print("Thank you for using Air!")
                    return
                if cmd == "HELP":
                    show_help()
                    continue
                if cmd == "CLEAR":
                    current_value = None
                    break  # volta pro topo e pede Num:
                if cmd == "HISTORY":
                    show_history(history)
                    continue

            print("-" * 40)
            print("Attention! Invalid operator. Use h for help.")
            print("-" * 40)

        # se deu CLEAR, volta ao topo
        if current_value is None:
            continue

        # 3) aplicar operador
        try:
            if op_kind == "UNARY_OP":
                before = current_value
                current_value = apply_unary(op_name, current_value)
                line = f"{op_name}({fmt(before)}) = {fmt(current_value)}"
                history.append(line)
                print(line)
                continue

            # binário: pedir próximo número (aceita ans = current_value)
            while True:
                kind, payload = parse_number(input("Num: "), ans=current_value)
                if kind == "NUMBER":
                    num2 = float(payload)
                    break

                if kind == "COMMAND":
                    cmd = str(payload)
                    if cmd == "QUIT":
                        print("-" * 40)
                        print("Thank you for using Air!")
                        return
                    if cmd == "HELP":
                        show_help()
                        continue
                    if cmd == "CLEAR":
                        current_value = None
                        break
                    if cmd == "HISTORY":
                        show_history(history)
                        continue

                print("-" * 40)
                print("Attention! Invalid number. Use h for help.")
                print("-" * 40)

            if current_value is None:
                continue

            before = current_value
            current_value = apply_binary(op_name, before, num2)
            line = f"{fmt(before)} {op_name} {fmt(num2)} = {fmt(current_value)}"
            history.append(line)
            print(line)

        except ZeroDivisionError:
            print("-" * 40)
            print("Attention! Can't divide by zero.")
            print("-" * 40)

        except ValueError as e:
            print("-" * 40)
            print(f"Attention! {e}")
            print("-" * 40)