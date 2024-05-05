import textwrap

def menu():
    menu = """ \n

    [1]\t Depositar
    [2]\t Sacar
    [3]\t Extrato
    [4]\t Nova conta
    [5]\t Novo usuário
    [0]\t Sair

    => """

    return input(textwrap.dedent(menu))

    
def deposito(saldo, valor, extrato, /):

    if valor <= 0:
        print("Depósito inválido, precisa ser um valor positivo! Digite novamente!")
    else:
        saldo += valor
        print("Depósito feito com sucesso! O novo saldo é: R$", saldo)
        extrato += f"Depósito R$ {valor:.2f}\n"
      
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    excedeu_limite_saldo = valor > saldo     
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > LIMITE_SAQUES
    
    if excedeu_limite_saldo:
        print("\n Operação inválida, você não possui saldo suficiente!")

    elif excedeu_limite:
        print("\n Operação inválida! O limite por saque é R$ 500.00")

    elif excedeu_saques:
        print("\n Número diário de saques atingido! Retorne amanhã!")
              
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso!  O seu novo saldo é: R$", saldo)

    else:
        print("\n Operação falhou, o valor é inválido!") 

    return saldo, extrato

def mostrar_extrato(saldo, / ,  * , extrato):

    print("\n ******* Olá, veja o seu extrato diário *******")
    print("\n Não ocorreram movimentações hoje." if not extrato else extrato)
    print(f"\n Saldo:\t R$ {saldo:.2f}")
    print("\n **********************************************")

def criar_usuario(usuarios):

    cpf = int(input("Informe somente os números do seu CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Esse CPF já está cadastrado")
        return
    
    nome = input("Informe o seu nome: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input(
        "Informe o endereço(logradouro, nro - bairro - cidade/estado): "
    )

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})
    print("Cadastro bem-sucedido")

def filtrar_usuario(cpf, usuarios):
    usuarios_existentes = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_existentes[0] if usuarios_existentes else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF:")
    usuario_existente = filtrar_usuario(cpf, usuarios)

    if usuario_existente:
        print("\n Conta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario_existente}

    else:
        print("\n Usuário não encontrado!")


def main():

    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite_saque_saldo = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas_usuarios = []
    num_contas = 0

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor que vai depositar: "))
            saldo, extrato = deposito(saldo, valor, extrato)
            
        elif opcao == "2":
            valor = float(input("Informe o valor a ser sacado: "))
            saldo, extrato = saque(saldo = saldo, valor = valor, extrato = extrato, limite = limite_saque_saldo , numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES)
                    
        elif opcao == "3":
            extrato = mostrar_extrato(saldo, extrato = extrato)

        elif opcao == "4":
            conta = criar_conta(AGENCIA, num_contas, usuarios)
            num_contas = len(contas_usuarios) + 1

            if conta:
                contas_usuarios.append(conta)

                        
        elif opcao == "5":
            criar_usuario(usuarios)
        
        elif opcao == "0":
            break
      
        else:
            print("Operação inválida!") 

main()          

