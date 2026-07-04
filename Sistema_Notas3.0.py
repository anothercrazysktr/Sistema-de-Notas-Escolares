print("Bem vindo ao Notas Master 3.0")
nomes = []
notas = []
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
                nomes.append (nome)
                break
#Loop de cadastro de notas - se você consegue ler isso ta me devendo 10 reais
        while True:
            nota = int(input("Qual a nota do aluno? "))
            if nota < 0 or nota > 10:
                print("Entrada inválida, insira uma nota de 0 a 10")
            else:
                print("Nota Cadastrada com sucesso")
                notas.append (nota)
                break
    elif cadastrar =="N":
        print("Fim do Cadastro")
        break
    else:
        print("Entrada inválida, tente novamente")
while True:
    resultado = input("Deseja verificar o resultado do aluno? S/N?").upper()
    if resultado == "S":
        while True:
            nome = input("Qual o nome do aluno? ").upper()
            if nome in nomes:
                print("Aluno encontrado")
                index = nomes.index(nome)
                nota = notas[index]
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
                break
            else:
                print("Aluno não encontrado, tente novamente")
    elif resultado =="N":
        print("Programa encerrado")
        break
