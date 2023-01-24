import adivinha
import forca

print("********************************")
print("******Escolha o seu Jogo!******")
print("********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o Jogo?"))

if(jogo == 1):
    print("Jogando Forca")
elif(jogo == 2):
    print("Jogando Adivinhação")



