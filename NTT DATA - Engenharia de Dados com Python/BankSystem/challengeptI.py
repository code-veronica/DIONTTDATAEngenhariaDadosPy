menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 5000
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Por favor, informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Desculpe, a operação falhou. O valor informado é inválido.")
            
    elif opcao == "s":
        valor = float(input("Por favor, informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Desculpe, a operação falhou! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Desculpe, a operação falhou! O valor do saque excede o limite.")
        
        elif excedeu_saldo:
            print("Desculpe, a operação falhou! Número máximo de saques diário excedido.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1 
            print(f"\nSaque realizado de: R$ {saldo:.2f}")
            
        else:
            print("Desculpe, a operação falhou. O valor informado é inválido.")
            
    elif opcao == "e":
        print("\n=============== E X T R A T O ===============")
        print("Não foram realizadas movimentações :(" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================")
        
    elif opcao == "q":
        print("Have a great day!")
        break
    
    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.")