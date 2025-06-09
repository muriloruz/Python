import random as rd
import os


def gerarNumero(num):
	numero = rd.randint(0,num)
	return numero

def limparTela():
	os.system('cls' if os.name == 'nt' else 'clear')


max = int(input("Digite o limite máximo de número do adivinhador:\n"))

n = gerarNumero(max)

range = 3
acerto = False
while range>0:
	print(f"Você ainda tem {range} tentativa(s)") 
	chute = int(input(f"Digite um número entre 0 e {max} e veja se acertou o número aleátorio: \n"))
	if chute == n:
		print("\033[32mAcertou!\033[0m")
		acerto = True
		break
	elif chute > n:
		print("\033[31mErrou!\033[0m \n \033[33mDica: O número é menor que o seu chute\033[0m")
		print("")
	elif chute < n:
		print("\033[31mErrou!\033[0m \n \033[33mDica: O número é menor que o seu chute\033[0m")
		print("")
	else:
		print("Número inválido")
	range = range - 1

if acerto == True:
	print(f"Parábens!Você acertou o número, ele era: {n}")
else:
	print(f"Acabou as tentativas! o número era {n}")