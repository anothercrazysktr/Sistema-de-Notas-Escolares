while True:
    nome = input("Qual nome do Aluno?")
    if nome == "":
        print("Nome inválido")
    else:
        break
        
while True:
    nota = int(input("Qual a nota do Aluno?"))
    
    if nota < 0 or nota > 10:
        print("Nota inválida, insira uma nota de 0 a 10")
    else:
        break
    
if nota == 10:
    print("Excelente!")
    print(nome,"você foi aprovado com excelência, parabéns!")
elif nota >= 7:
    print("Aprovado")
    print(nome,"você foi aprovado!")

elif nota >= 5:
    print("Recuperação")
    print(nome,"precisa estudar mais na recuperação")

elif nota >= 0:
    print("Reprovado")
    print(nome,"você foi reprovado")
while True:
    continuar = input("Deseja continuar? (Sim ou Não?)")
    if continuar.upper() == "S":
        break
    elif continuar.upper() == "N":
        print("Programa encerrado")
        exit()
