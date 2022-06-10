#!/bin/python3

from math import log


def juros_compostos(PV: float = None, FV: float = None, I: float = None, N: int = None) -> float:
    if PV and I and N:
        # calcula FV
        return PV * (1 + I/100)**N
    elif FV and I and N:
        # calcula PV
        return FV/(1+I/100)**N
    elif PV and FV and N:
        # calcula I
        return (FV/PV)**(1/N)-1
    elif PV and FV and I:
        # calcula N
        return log(FV/PV)/log(1+I/100)
    else:
        raise "Deve-se passar no mínimo três argumentos"


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Calculo de juros compostos",
        epilog="""\
EXEMPLOS:
    calcular valor final
    $ juros_compostos -PV 400 -I 5 -N 3
    463.0500

    calcular valor presente
    $ juros_compostos -FV 463.05 -I 5 -N 3
    400.000

    calcular taxa
    $ juros_compostos -PV 400 -FV 463.05 -N 3
    5.0000%

    calcular periodo
    $ juros_compostos -PV 400 -FV 463.05 -I 5
    3

FORMULAS:
    FV = PV * (1 + I/100)**N
    PV = FV / (1 + I/100)**N
    I  = (FV/PV)**(1/N)
    N  = log(FV/PV) / log(1 + I/100)
    """,
    )

    parser.add_argument(
        "-PV", type=float, help="(Present Value) Valor presente antes do calculo de juros")
    parser.add_argument("-FV", type=float,
                        help="(Final Value) Valor final do calculo de juros")
    parser.add_argument("-I", type=float, help="Taxa de juros em porcentagem")
    parser.add_argument("-N", type=int, help="Periodo que será aplicado")

    parser.add_argument("-n", type=int, default=2,
                        help="Número de casas decimais")

    args = parser.parse_args()

    try:
        print(f"{ juros_compostos(PV=args.PV, FV=args.FV, I=args.I, N=args.N) :.{args.n}f}")
    except:
        parser.print_help()
