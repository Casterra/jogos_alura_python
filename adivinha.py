import random


print("********************************")
print("Bem vindo ao jogo de Adivinhaçao")
print("********************************")


numero_correto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?", numero_correto)
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

print(numero_correto)

for rodada in range (1,total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("digite um numero entre 1 e 100:")
    print("voce digitou", chute)
    chute = int(chute)

    if (chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100!")
        continue

    acertou = chute == numero_correto
    maior   = chute > numero_correto
    menor   = chute < numero_correto

    if(acertou):
        print("Voce acertou e fez {} pontos!" .format(pontos))
        break
    else:
        if(maior):
            print("Voce errou! O seu numero foi maior do que o numero secreto")
        elif(menor):
            print("Voce errou! O seu numero foi menor do que o numero secreto")
        pontos_perdidos = abs(numero_correto - chute) / 3
        pontos = pontos - pontos_perdidos


print("Fim de Jogo")




