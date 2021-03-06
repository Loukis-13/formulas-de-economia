#!/bin/python3

def elasticidade_demanda(Q1: float, Q2: float, P1: float, P2: float) -> float:
	""" (Q2/Q1-1) / (P2/P1-1) """
	return (Q2/Q1-1)/(P2/P1-1)


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(
		description="Calculo da elasticidade",
		epilog="FORMULA: (Q2/Q1-1) / (P2/P1-1)",
	)

	parser.add_argument("Q1", type=float, help="Quantidade 1")
	parser.add_argument("Q2", type=float, help="Quantidade 2")
	parser.add_argument("P1", type=float, help="Preço 1")
	parser.add_argument("P2", type=float, help="Preço 2")

	parser.add_argument("-n", type=int, default=4, help="Número de casas decimais")

	args = parser.parse_args()

	res = elasticidade_demanda(args.Q2, args.Q1, args.P2, args.P1)

	print(f"{ res :.{args.n}f}")

	if res < 1:
		print("Inelástica")
	elif res > 1:
		print("Elástica")
	else:
		print("Unitária")
