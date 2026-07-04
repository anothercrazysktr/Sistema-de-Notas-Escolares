#Adição de Nomes
nomes = []
while True:
    nome = input("Qual nome do Aluno?")
    
    if nome == "":
        print("Nome inválido")
    else:
        nomes.append(nome)
        break

#Adição de Notas
notas =[]   
while True:
    nota = int(input("Qual a nota do Aluno?"))
    
    if nota < 0 or nota > 10:
        print("Nota inválida, insira uma nota de 0 a 10")
    else:
        notas.append(nota)
        break
#Resultado de Notas
if nota == 10:
    print("Excelente!")
    print(nomes[0],"você foi aprovado com excelência, parabéns!")
elif nota >= 7:
    print("Aprovado")
    print(nomes[0],"você foi aprovado!")

elif nota >= 5:
    print("Recuperação")
    print(nomes[0],"precisa estudar mais na recuperação")

elif nota >= 0:
    print("Reprovado")
    print(nomes[0],"você foi reprovado")

print("Cadastro finalizado")

while True:
    print("Deseja cadastrar mais um aluno? Sim ou Não?")
    if input() == ("Sim"):
        nome = input("Qual o nome do Aluno?")
        if nome == "":
            print("Nome inválido")
        else:
            nomes.append(nome)
        nota = int(input("Qual a nota do Aluno?"))
        if nota == 10:
            print("Excelente!")
            print(nomes[0+1],"você foi aprovado com excelência, parabéns!")
        elif nota >= 7:
            print("Aprovado")
            print(nomes[0+1],"você foi aprovado!")
        elif nota >= 5:
            print("Recuperação")
            print(nomes[0+1],"precisa estudar mais na recuperação")
        elif nota >= 0:
            print("Reprovado")
            print(nomes[0+1],"você foi reprovado")
        else:
            notas.append(nota)
            print("Cadastro finalizado")
            break
    if input() == ("Não"):
        (print("Programa encerrado"))
        break
