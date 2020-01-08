from random import randint
from time import sleep
jogador = int(input("Em que numero eu pensei: ")) # Jogador tena adivinhar o número que o computador "pensou"
computador = randint(0, 3)# Computador "pensa" alenatoriamente de 1 a 3
print("Processando...")
sleep(0.5)
if jogador == computador:
    print("Parabens! Voce conseguiu me vencer")
else:
    print(f"Ganhei! Eu pensei no número {computador} e não no {jogador}")
