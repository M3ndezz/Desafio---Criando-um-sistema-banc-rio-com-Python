# Tela inicia que mostra para o usuário a opção de criar usuário e logar conta
def tela_inicial_conta():
    account = """====== Bem vindo ao Banco DIO ======
        Digite abaixo o número desejado!

            [1] Criar usuário
            [2] Logar conta

====================================
=>  """
    return account

# 1° Criar usuário, pedindo informações básica (sem autentificação)
# linha 20 armazena os dados em um lista de dicionário, linha 21 chama a função criar_conta
def criar_usuario(dados_usuario, dados_conta):
    nome = input("Digite o seu nome:")
    nascimento = input("Digite a sua data de nascimento sem hifén ou barra: ")
    cpf = input("Digite o seu CPF: ")
    endereco = input("Digite o seu endereço: ")
    dados_usuario.append({"Nome": nome, "Nascimento": nascimento, "CPF": cpf, "Endereço": endereco})
    criar_conta(dados_conta)

    return dados_usuario, dados_conta

# criará agência e conta automaticamente
def criar_conta(dados_conta):
    agencia = "0001"
    conta = len(dados_conta) + 1        # Ele verá o tamanho da lista e acrescetará +1
    print(f"O n° da sua agência {agencia}\n"
          f"O n° da sua conta {conta}")
    dados_conta.append({"Nº da Agência": agencia, "Nº da conta": conta})

    return dados_conta

# Tela inicia que mostra para o usuário a opção de Depósito, Saque, Extrato e Sair
def tela_inicial():
    menu = """====== Bem vindo ao Banco DIO ======
    Digite abaixo o número desejado!

        [1] Depósito
        [2] Saque
        [3] Extrato
        [4] Sair

====================================
=>  """
    return menu

# A função Sacar, com a regra de por nome, definido pelo *
def sacar(*, saldo, valor, extrato, numero_saque, limitado_saque, limite):      # Apenas por nome
    if saldo < valor:
        print("Valor abaixo do saldo, por favor digite o valor corretamente para sacar!")

    elif numero_saque == limitado_saque:
        print("Você já atingiu o limite de saque diário, por favor aguarde até o outro dia!")

    elif valor <= limite:
        numero_saque += 1
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        print("Retire na boca do caixa!")

    return saldo, extrato, numero_saque, limitado_saque, limite

# A função Depositar, com a regra de por posição, definido pelo /
def depositar(saldo, saldo_real, extrato, /):       # Apenas por posição /
    if saldo_real > 0:
        saldo += saldo_real
        extrato += f"Depósito:\tR$ {saldo_real:.2f}\n"
        print("\nDepósito feito com sucesso!")
    else:
        print("\nFalha no depósito, tente novamente!")

    return saldo, extrato

# A função saldo, com a regra de por nome e posição, / e *
def extrato_bancario(saldo, /, *, extrato):     # Posição e nome * /
    print("\n==========Extrato==========")
    if not extrato:
        print("\nNão foram realizadas movimentações.")
    else:
        print(f"\n{extrato}")
        print(f"\nO seu saldo atual: {saldo:.2f}")
        print("\n===========================")

    return saldo, extrato

# A função principal, onde tudo se incia para começar a operação do códigos
def variavel():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    limitado_saque = 3
    dados_usuario = []
    dados_conta = []
    todos_dados = []

# While, para começar na tela_incial_conta, após logar o while será quebrado
    while True:
        clicar = input(tela_inicial_conta())

        if clicar == "1":
            print("\nOpção de criar usuário selecionado...\n")

            # Chamará a função criar_usuário, após terminar a operação na função, irá mesclar tudo em todos_dados

            criar_usuario(dados_usuario, dados_conta)
            todos_dados = dados_usuario + dados_conta

        elif clicar == "2":
            print("\nOpção de logar conta selecionado...\n")

            # Selecionar o logar conta, começará o processo de input de alguns dados

            nome_usuario = input("Digite seu nome de usuário: ")
            cpf = input("Digite seu CPF: ")

            # Processo de autenticação da informações inseridas

            usuario_encontrado = False      # Definir a variavel de confirmação com False
            for usuario in todos_dados:     # Inicia um for de para atutenticação

                # Ele irá consultar pelo .get, e irá fazer uma comparação com valor do input

                if usuario.get("Nome") == nome_usuario and usuario.get("CPF") == cpf:

                    # Caso, os dados estejam correto a variavel usuario_encontrado se tornará True

                    usuario_encontrado = True

            if usuario_encontrado:
                print("Usuário autenticado com sucesso!")
                break
            else:
                print("Nome de usuário ou senha incorretos.")

        # Caso o usuário digite o numero errado
        else:
            print("\nNumero errado, por favor selecione corretamente\n")

    # Iniciará outro While após o login for feito e começará com tela_inicial
    while True:
        opcao = input(tela_inicial())

        # Opção 1 selecionará opção depósito

        if opcao == "1":
            print("\nOpção de depósito selecionado...")
            print()
            saldo_real = float(input("Informe o seu valor do depósito: "))

            # Função depositar com argumentos saldo, saldo_real e extrato para operar
            # A regra por posição

            saldo, extrato = depositar(saldo, saldo_real, extrato)

        # Opção 2 selecionará opção saque com argumento saldo, valor, extrato, numero_saque, limitado_saque e limite
        # A regra por nome

        elif opcao == "2":
            print("\nOpção de saque selecionado...")
            print()
            valor = float(input("Quanto deseja sacar: "))

            saldo, extrato, numero_saque, limitado_saque, limite = sacar(saldo=saldo,
                                                                         valor=valor,
                                                                         extrato=extrato,
                                                                         numero_saque=numero_saque,
                                                                         limitado_saque=limitado_saque,
                                                                         limite=limite)

        # Opção 3 selecionará opção extrato com argumento, saldo e extrato
        # A regra por posição e nome

        elif opcao == "3":
            print("\nOpção de extrato selecionado...")
            print()
            saldo, extrato = extrato_bancario(saldo, extrato=extrato)

        # Opção 4 sair, encerrará o código!

        elif opcao == "4":
            print("Saindo da conta...")
            print("Obrigado por ser nosso cliente!")
            break

        # Caso o usuário digite o numero errado

        else:
            print("Numero errado, por favor selecione corretamente")


variavel()      # Chamada da variavel, onde começara o programa
