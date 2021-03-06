#!/bin/python3

def taxa_efetiva(I: float, Q: float) -> float:
    """ ( (1 + (i/100) / q)**q-1 ) * 100 """
    return (1+(I/100)/Q)**Q-1


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Calculo da taxa efetiva",
        epilog="FORMULA: ( (1 + (i/100) / q)**q-1 ) * 100",
    )

    parser.add_argument("I", type=float, help="Taxa")
    parser.add_argument("Q", type=float, help="Periodo")

    parser.add_argument("-n", type=int, default=4, help="Número de casas decimais")

    args = parser.parse_args()

    print(f"{ taxa_efetiva(args.I, args.Q) :.{args.n}%}")
