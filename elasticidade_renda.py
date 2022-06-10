#!/bin/python3

def elasticidade_renda(Q1: float, Q2: float, R1: float, R2: float) -> float:
    """ (Q2/Q1-1) / (R2/R1-1) """
    return (Q2/Q1-1)/(R2/R1-1)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Calculo da elasticidade",
        epilog="FORMULA: (Q2/Q1-1) / (R2/R1-1)",
    )

    parser.add_argument("Q1", type=float, help="Quantidade 1")
    parser.add_argument("Q2", type=float, help="Quantidade 2")
    parser.add_argument("R1", type=float, help="Renda 1")
    parser.add_argument("R2", type=float, help="Renda 2")

    parser.add_argument("-n", type=int, default=4, help="Número de casas decimais")

    args = parser.parse_args()

    res = elasticidade_renda(args.Q2, args.Q1, args.R2, args.R1)

    print(f"{ res :.{args.n}f}")

    if 0 < res <= 1:
        print("Bem normal")
    elif res > 1:
        print("Bem superior")
    elif res < 0:
        print("Bem inferior")
    elif res == 0:
        print("Bem de consumo saciado")
