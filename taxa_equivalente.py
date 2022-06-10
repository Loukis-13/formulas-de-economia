#!/bin/python3

def taxa_equivalente(it: float, Q: int, T: int) -> float:
    """ ( (1 + it/100)**(Q/T) -1 ) * 100 """
    return ((1+it/100)**(Q/T)-1)*100


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Calcula a equivalência de taxas.",
        epilog="FORMULA: ( (1 + it/100)**(Q/T) -1 ) * 100",
    )

    parser.add_argument("it", type=float, help="Taxa do período que se tem")
    parser.add_argument("T", type=int, help="Prazo da taxa que se tem")
    parser.add_argument("Q", type=int, help="Prazo da taxa que se quer")

    parser.add_argument("-n", type=int, default=4, help="Número de casas decimais")

    args = parser.parse_args()

    print(f"{ taxa_equivalente(args.it, args.Q, args.T) :.{args.n}%}")
