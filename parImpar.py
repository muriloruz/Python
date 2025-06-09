import random as rd
import os
def gerarNumero():
	nRand = rd.randint(0,9)
	return nRand

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
	print("Bem vindo ao jogo de par ou impar!")
	op = input("Digite qual você deseja: ímpar ou par\n")
	time = " "
	nAleatorio = 0
	match op.lower():	
		case "par":
			time = "Par"
			nAleatorio = gerarNumero()
			break;
		case "ímpar" | "impar":
			time = "Impar"
			nAleatorio = gerarNumero()
			break;
		case _:
			limpar_console()
			print("ERROR, opção inválida")
			

n = int(input(f"Digite um número: "))
soma = nAleatorio+n
if soma%2==0 and time=="Par":
	print(f"Seu número é {n} e o número da IA é {nAleatorio} o resultado é {soma}")
	print("Ganhou!")
elif soma%2==1 and time =="Impar":
	print(f"Seu número é {n} e o número da IA é {nAleatorio} o resultado é {soma}")
	print("Ganhou!")
else:
	print(f"Seu número é {n} e o número da IA é {nAleatorio} o resultado é {soma}")
	print("Perdeu")

