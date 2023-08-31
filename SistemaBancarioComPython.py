## DESCRIÇÃO

##Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. O objetivo é implementar três operações essenciais: depósito, saque e extrato. 
##O sistema será desenvolvido para um banco que busca monetizar suas operações. 
##Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. 
##Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.

# Nao precisa guardar o dono da conta. e mono usuario
## Deposito
# Depositar valores positivos na conta corrente;
# Todos os depositos devem ser armazenados em uma variavel e exibidos na operacao de extrato;

# saques
# O sistema deve permitir realizar 3 saques diarios com limite maximo de 500 reais por saque.  
# Caso o usuario nao tenha saldo o sistema deve exibir uma mensagem informando que nao será possivel sacar o dinhjeiro por falta de saldo.
# Todos os saques devem ser armazenados em uma variavel e exibidos na operacao de extrato;

# Extrato
# A operacao deve listar todos os depositos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da Conta. OS valores devem ser exibidos no formato R$ XXX.XX - 1500.45 - R$ 1500.45


menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
      print("deposito")
      valor = float(input("Informe o valor do deposito: "))
      if valor > 0:
            saldo += valor
            extrato += f"(+) Deposito + : R$ {valor:.2f}\n" 
      else: 
        print("Desposito: Operacao falhou! O valor informado e invalido.")

    elif opcao == "s":
      print("Saque")

      valor = float(input("Informe o valor do saque: "))

      excedeu_saldo = valor > saldo

      excedeu_limite = valor > limite

      excedeu_saques = numero_saques >= LIMITE_SAQUES

      if excedeu_saldo:
         print(f"Saque: Operacao falhou! Voce nao tem saldo suficiente! Saldo atual: R$ {saldo:.2f}.")

      elif excedeu_limite:
         print("Saque: Operacao falhou! O valor do saque e maior que o limite!")

      elif excedeu_saques:
         print("Saque: Operacao falhou! Numero de saque excedido!")   

      elif valor > 0:
         saldo -= valor
         extrato += f" (-) Saque  - : R$ {valor:.2f}\n" 
         numero_saques += 1
      else:
         print("Saque: Operacao falhou! O valor informado e invalido!")

    elif opcao == "e":
      print("########### Extrato ################")
      print("Nao foram realizados movimentacoes" if not extrato else extrato)
      print("-------------------------------------")
      print(f"\nSaldo atual: R$ {saldo:.2f} ")
      print("########### FIM Extrato #############")

    elif opcao == "q":
      break
    else:
      print("Operacao invalida! Favor selecionar novamente a operacao desejada.")
