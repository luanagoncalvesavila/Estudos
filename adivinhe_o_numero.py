#	Jogo - adivinhe o número

import random

def adivinhe(x):
	numero_aleatorio = random.randint(1, x)
	adivinhe = 0
	while adivinhe != numero_aleatorio:
		adivinhe = int(input(f"Adivinha qual número estou pensando entre 1 e {x}: "))
		if adivinhe < numero_aleatorio:
			print("Mais...")
		elif adivinhe > numero_aleatorio:
			print("Menos...")
	print(f"Uhuuuul, acertou! É {numero_aleatorio} mesmo!")



adivinhe(100)