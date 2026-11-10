import urllib.request
import json

alunos = {}
cep = {}

def consultar_cep():
    # Loop de Consulta de CEP
    while True:
        cep_digitado = input("Qual CEP deseja consultar? ").strip()
        
        # Remove traços ou espaços caso o usuário digite (ex: 03647-050)
        cep_digitado = cep_digitado.replace("-", "").replace(" ", "")
        
        if cep_digitado == "":
            print("Entrada inválida, tente novamente")
        else:
            url = f"https://brasilapi.com.br/api/cep/v2/{cep_digitado}"
            try:
                # Cria uma requisição simulando um navegador para evitar bloqueios
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                
                with urllib.request.urlopen(req) as resposta:
                    conteudo = resposta.read().decode('utf-8')
                    dados_cep = json.loads(conteudo)
                    
                    # Extrai os campos que a BrasilAPI devolveu
                    rua = dados_cep.get('street', 'Não informado')
                    bairro = dados_cep.get('neighborhood', 'Não informado')
                    cidade = dados_cep.get('city', 'Não informado')
                    estado = dados_cep.get('state', 'Não informado')
                    
                    print("\n=== Endereço encontrado ===")
                    print(f"Rua: {rua}")
                    print(f"Bairro: {bairro}")
                    print(f"Cidade/UF: {cidade}/{estado}")
                    print("===========================\n")
                    break
                    
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print("Erro: CEP não encontrado na base de dados. Tente novamente.\n")
                else:
                    print(f"Erro de servidor da API (Código {e.code}). Tente novamente.\n")
            except Exception as e:
                print(f"Erro inesperado de conexão: {e}. Tente novamente.\n")

def cadastrar_aluno(alunos):
    proximo_id = len(alunos) + 1
    # Loop de Cadastro de nomes
    while True:
        nome = input("Qual o nome do aluno? ").upper()
        if nome == "":
            print("Entrada inválida, tente novamente")
        else:
            print("Aluno Cadastrado")
            break
            
    # Loop de cadastro de notas
    while True:
        nota = int(input("Qual a nota do aluno? "))
        if nota < 0 or nota > 10:
            print("Entrada inválida, insira uma nota de 0 a 10")
        else:
            print("Nota Cadastrada com sucesso")
            alunos[nome] = nota
            break

def consultar_nota(alunos):
    #Loop de Consulta de Notas
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

#Menu Novo
while True:
    print("\n--- MENU Notas Master 4.0 ---")
    print("[1] Cadastrar Aluno")
    print("[2] Consultar nota do Aluno")
    print("[3] Consultar Endereço")
    print("[4] Sair")

# Input do Usuário
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("Você escolheu cadastrar!")
        cadastrar_aluno(alunos)
        
    elif opcao == "2":
        print("Você escolheu consultar!")
        consultar_nota(alunos)
        
    elif opcao == "3":
        consultar_cep()
        
    elif opcao == "4":
        print("Saindo do programa...")
        break
        
    else:
        print("Opção inválida! Digite 1, 2 ou 3.")