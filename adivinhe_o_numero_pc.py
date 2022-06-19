# Jogo - PC adivinha o número
# -*- coding: utf-8 -*-
import random
def palpite(x):
	a = 1
	b = x
	retorno = ''

	while retorno != 'c':
		if a != b:
			chute = random.randint(a, b)
		else:
			chute = a # tanto faz
		print(f"Eu diria que você pensou no número {chute}.")
		retorno = input(f"{chute} é maior (A), menor (E) ou é o número que você pensou (C)?").lower()
		if retorno == 'e':
			chute = chute - 1
		elif retorno == 'a':
			chute = chute + 1

print("Robô 1 X 0 Humanos")
palpite(100)