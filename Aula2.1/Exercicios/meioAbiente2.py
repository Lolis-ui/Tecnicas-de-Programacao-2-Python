op = input("Digite o índice de poluição: ")

match op: 
    case 1:
        op <= 2
        print("Considerável aceitável")
    case 2: 
        op >= 3 and op <=5
        print('Suspender Atividades Grupo1')
    case 3: 
        op == 6|7
        print("Suspender Atividades Grupo2")
    case _: 
        op >= 8
        print("suspender atividade de todos os grupos")
    