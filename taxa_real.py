#!/bin/python3

def taxa_real(IN: float, I: float) -> float:
    """ ( (1 + IN/100) / (1 + I/100) -1 ) * 100 """
    return (1+IN/100)/(1+I/100)-1


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Calcula o valor da taxa real.",
        epilog="FORMULA: ( (1 + IN/100) / (1 + I/100) -1 ) * 100",
    )

    parser.add_argument("IN", type=float, help="Taxa de juros nominal em porcentagem")
    parser.add_argument("I", type=float, help="Taxa de inflação em porcentagem")

    parser.add_argument("-n", type=int, default=4, help="Número de casas decimais")

    args = parser.parse_args()

    print(f"{ taxa_real(args.IN, args.I) :.{args.n}%}")
