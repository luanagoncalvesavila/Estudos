# Jogo - Papel, tesoura ou pedra, in english

import random

def jogo():
	user = input("'R' for ROCK, 'P' for PAPER, 'S' for SCISSORS, 'L' for LIZARD and 'K' for SPOCK. Choose your weapon: ").lower()
	pc = random.choice(['r', 'p', 's', 'l', 'k'])

	if user == pc:
		return 'It\'s a tie!'

	if vitoria(user, pc):
		return "You won!"
	
	return "You lost!"

def vitoria(tu, ele):
	if (tu == 'r' and ele == 's') or (tu == 's' and ele == 'p') or (tu == 'p' and ele == 'r') or (tu == 'r' and ele == 'l') or (tu == 'l' and ele == 'k') \
	 or (tu == 'k' and ele == 's') or (tu == 'k' and ele == 'r') or (tu == 'l' and ele == 'p') or (tu == 's' and ele == 'l'):
		return True

print(jogo())