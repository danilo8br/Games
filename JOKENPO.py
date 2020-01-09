from random import randint
from time import sleep
itens = ("\033[1;34mPedra\033[m", "\033[1;32mPapel\033[m", "\033[1;35mTesoura\033[m")
computador = randint(0, 2)
print("""\033[1;33mSuas opções:\033[m                     
[\033[1;34m0\033[m] \033[1;34mPEDRA\033[m
[\033[1;32m1\033[m] \033[1;32mPAPEL\033[m
[\033[1;35m2\033[m] \033[1;35mTESOURA\033[m""") # Cores em python
print("-=" * 15)
jogador = int(input("Faça sua jogada: "))
print("\033[1;32mJO\033[m")
sleep(1.0)
print("\033[1;35mKEN\033[m")
sleep(1.0)
print("\033[1;34mPO\033[m")
sleep(1.0)
print("-=" * 15)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print("EMPATE!")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")        
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")            
    elif jogador == 2:
        print("EMPATE!")    
    else:
        print("JOGADA INVÁLIDA")
