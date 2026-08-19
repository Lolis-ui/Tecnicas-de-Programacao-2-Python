#Comando para limpar tela
import os
os.system("cls")

entrada = input("você quer entrar ou sair? ")
#Comando de decisão IF
if entrada == "entrar":
    print('Você entrou no sistema')
elif entrada == "sair": 
    print("você saiu do sistema")
else: 
    print("Coloque entrar ou sair")
