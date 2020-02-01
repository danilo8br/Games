from random import randint

v = 0

while True:
    computador = randint(0, 10)
    jogador = int(input("Digite um numero: "))
    total = computador + jogador
    opcao = " "
    while opcao not in "PpIi":
        opcao = str(input("Par ou Impar? [P/I]")).strip().upper()[0]
        print(f"Voce jogou {jogador} e o computador {computador}. Total de {total}")
        print(f"DEU PAR" if total % 2 == 0 else "DEU IMPAR")
    if opcao == "P":
        if total % 2 == 0:
            print("Voce venceu")
            v += 1
        else:
            print("Voce perdeu")
            break
    elif opcao == "I":
        if total % 2 == 1:
            print("Voce venceu")
            v += 1
        else:
            print("Voce perdeu")
            break
    print("Vamos jogar novamente")
print(f"Gamer Over! Voce venceu {v} vezes")
