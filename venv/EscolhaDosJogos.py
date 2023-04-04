import testecomFor
import forca

def escolhe_jogo():
 print("*********************************")
print("*****Esoclha o seu jogo!*********")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo deseja jogar?"))

if (jogo == 1):
    print("inciando Forca")
    forca.jogar()
elif (jogo == 2):
    print("Iniciando Adivinhação")
testecomFor.jogar()

if(__name__=="__main__"):
    escolhe_jogo()
