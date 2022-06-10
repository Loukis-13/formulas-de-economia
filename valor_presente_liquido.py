#!/bin/python3

from decimal import Decimal
from typing import List


def valor_presente_liquido(FCO: float, FC: List[float], I: float) -> float:
    """ sum(FC[i]/(1+I/100)**i for i in range(1,len(FC)+1)) - FCO """
    return sum(v/(1+I/100)**i for i, v in enumerate(FC, 1)) - FCO

def TIR(FCO: float, FC: List[float]) -> float:
    FCO, FC = Decimal(FCO), [*map(Decimal, FC)]
    x, y = Decimal(0), Decimal(1)
    f = False

    s = sum(v/(1+x/100)**i for i, v in enumerate(FC, 1)) - FCO

    if abs(s) < 1e-5:
        return x
    
    if s < 0:
        y = -y
        f = True

    for _ in range(200):
        s = sum(v/(1+(x+y)/100)**i for i, v in enumerate(FC, 1)) - FCO
        
        if abs(s) < 1e-5:
            x += y
            break

        if (s > 0 and not f) or (s < 0 and f):
            x += y
        else:
            y /= 10
        
    return x


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Calcula o valor presente líquido",
        epilog="FORMULA: sum(FC[i]/(1+I/100)**i for i in range(1,len(FC)+1)) - FCO",
    )

    parser.add_argument("-I", type=float, help="Taxa")
    parser.add_argument("-FCO", type=float, help="Valor do investimento inicial")
    parser.add_argument("-FC", type=float, nargs="+", help="Fluxo de caixa")
    parser.add_argument("-TIR", action='store_true', help="Calcula a taxa interna de retorno")

    parser.add_argument("-n", type=int, default=4, help="Número de casas decimais")

    args = parser.parse_args()

    print(f"{ valor_presente_liquido(args.FCO, args.FC, args.I) :.{args.n}f}")

    if args.TIR:
        print(f"{TIR(args.FCO, args.FC) :.{args.n}f}")
