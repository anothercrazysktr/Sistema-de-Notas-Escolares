print("Bem vindo ao Notas Master 3.0")
nomes = []
notas = []
#Loop Meste
while True:
    resposta = input("Deseja cadastrar um aluno? S/N? ").upper()
    if resposta == "S":
#Loop de Cadastro de nomes
        while True:
            nome = input("Qual o nome do aluno? ")
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
    elif resposta =="N":
        print("Fim do Cadastro")
        break
    else:
        print("Entrada inválida, tente novamente")