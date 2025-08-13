from typing import List
from time import sleep

from Projeto_Banco.models.cliente import Cliente
from Projeto_Banco.models.conta import Conta


contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    while True:
        print("=========================================")
        print("================== ATM ==================")
        print("============ Generic Bank ===============")
        print("=========================================")

        print("Selecione uma opção no menu:")
        print("1 - Criar conta")
        print("2 - Efetuar saque")
        print("3 - Efetuar depósito")
        print("4 - Efetuar transferencia")
        print("5 - Listar contas")
        print("6 - Sair do sistema")

        try:
            opcao: int = int(input())

            if opcao == 1:
                criar_conta()
            elif opcao == 2:
                efetuar_saque()
            elif opcao == 3:
                efeutar_deposito()
            elif opcao == 4:
                efetuar_transferencia()
            elif opcao == 5:
                listar_contas()
            elif opcao == 6:
                print("Volte sempre")
                sleep(2)
                exit(0)
            else:
                print("Opção inválida")
                sleep(2)
                menu()
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")
            sleep(2)

def criar_conta() -> None:
    print("Informe os dados do cliente: ")

    nome: str = input("Nome do Cliente: ")
    email: str = input("E-mail do cliente: ")
    cpf: str = input("CPF do cliente: ")
    data_nascimento: str = input("Data de nascimento do cliente: ")

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)


def efetuar_saque() -> None:
    pass


def efeutar_deposito() -> None:
    pass


def efetuar_transferencia() -> None:
    pass


def listar_contas() -> None:
    pass


def buscar_conta_por_numero(numero: int) -> Conta:
    pass


if __name__ == '__main__':
    main()

