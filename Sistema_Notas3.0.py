print("Bem vindo ao Notas Master 3.65")
alunos = {}
#Loop Meste 
while True:
    cadastrar = input("Deseja cadastrar um aluno? S/N? ").upper()
    if cadastrar == "S":
#Loop de Cadastro de nomes
        while True:
            nome = input("Qual o nome do aluno? ").upper()
            if nome == "":
                print("Entrada inválida, tente novamente")
            else:
                print("Aluno Cadastrado")
                break
#Loop de cadastro de notas - se você consegue ler isso ta me devendo 10 reais
        while True:
            nota = int(input("Qual a nota do aluno? "))
            if nota < 0 or nota > 10:
                print("Entrada inválida, insira uma nota de 0 a 10")
            else:
                print("Nota Cadastrada com sucesso")
                alunos[nome] = nota
                break
    elif cadastrar =="N":
        print("Fim do Cadastro")
        break
    else:
        print("Entrada inválida, tente novamente")

#Pesquisa de Notas
while True:
    resultado = input("Deseja verificar o resultado do aluno? S/N?").upper()
    if resultado == "S":
        while True:
            nome = input("Qual o nome do aluno? ").upper()
            if nome in alunos:
                print("Aluno encontrado")
                nota = alunos[nome]
                if nota == 10:
                    print("Excelente!")
                    print(f"{nome}, você tirou {nota} e foi aprovado com excelência, parabéns!")
                elif nota >= 7:
                    print("Aprovado")
                    print(f"{nome}, tirou {nota} e foi aprovado!")
                elif nota >= 5:
                    print("Recuperação")
                    print(f"{nome}, você tirou {nota} e precisa estudar mais na recuperação")
                elif nota >= 0:
                    print("Reprovado")
                    print(f"{nome} tirou {nota} e você foi reprovado")
                break
            else:
                print("Aluno não encontrado, tente novamente")
    elif resultado =="N":
        print("Programa encerrado, obrigado por utilizar o Notas Master 3.65")
        break
