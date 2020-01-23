from random import randint

computador = randint(0, 10)
print("Ola, sou seu computador... Acabei de pensar em um numero de 0 a 10")
print("Sera que você consegue adivinhar qual foi?")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual seu palpite: ")
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
           print("Mais...")
        elif jogador > computador:
           print("Menos...")
print(f"\033[1;34mAcertou com {palpites} tentativas\033[m")
            
            
