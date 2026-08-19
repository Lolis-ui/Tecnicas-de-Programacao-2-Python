sexo = input("Digite o seu sexo (Masculino ou Feminino): ")
altura = float(input("Digite a sua altura (em metros): "))

if sexo.lower() == "masculino":
    pesoIdeal = (72.7 * altura) - 58
    print(f"O seu peso ideal é: {pesoIdeal:.2f} kg")
elif sexo.lower() == "feminino":
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é: {pesoIdeal:.2f} kg")
else:
    print("Resposta inválida! Digite 'Masculino' ou 'Feminino'.")