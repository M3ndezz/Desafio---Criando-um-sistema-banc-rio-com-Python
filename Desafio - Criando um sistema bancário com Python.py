menu = """====== Bem vindo ao Banco DIO ======
   Digite abaixo o número desejado!
    
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Sair

====================================
=>  """

saldo = 0
limite = 500
extrato = []
numero_saque = 0
LIMITADO_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("\nOpção de depósito selecionada...")
        print()
        saldo = float(input("Quanto deseja depositar > "))
        extrato.append({"tipo": "depósito", "valor": saldo})

    elif opcao == "2":
        print("\nOpção de saque selecionada...")
        print()
        valor = float(input("Quanto deseja sacar > "))

        if saldo <= valor:
            print("Valor abaixo do saldo, por favor digite o valor corretamente para sacar!")

        elif numero_saque == LIMITADO_SAQUES:
            print("Você já atingiu o limite de saque diário, por favor aguarde até o outro dia!")

        elif valor <= limite:
            numero_saque += 1
            saldo -= valor
            print("Retire na boca do caixa!")
            extrato.append({"tipo": "saque", "valor": valor})

        else:
            print(f"O seu limite é {limite:.2f} reais, por favor digite outro valor!")

    elif opcao == "3":
        print("\n==========Extrato==========")
        for transacao in extrato:
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f'\n{tipo}: R$ {valor:.2f}')
        print(f"\nO seu saldo atual é R$ {saldo:.2f}")
        print("\n===========================")

    elif opcao == "4":
        print("Saindo da conta...")
        print("Obrigado por ser nosso cliente!")
        break

    else:
        print("Operação inválida, por favor seleciona a opção desejada corretamente!")