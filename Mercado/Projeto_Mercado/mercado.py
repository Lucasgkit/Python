from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()

def menu() -> None:
    while True:
        print("==================================")
        print("========== Bem-vindo(a) ==========")
        print("=========   Name Shop   ==========")
        print("==================================")
        print("Selecione uma opção abaixo: ")
        print("1 - Cadastrar produto")
        print("2 - Listar produto")
        print("3 - Comprar produto")
        print("4 - Visualizar carrinho")
        print("5 - Fechar pedido")
        print("6 - Sair do sistema")

        try:
            opcao: int = int(input("Digite a opção desejada: "))

            if opcao == 1:
                cadastrar_produto()
                break
            elif opcao == 2:
                listar_produtos()
                break
            elif opcao == 3:
                comprar_produto()
                break
            elif opcao == 4:
                visualizar_carrinho()
                break
            elif opcao == 5:
                fechar_pedido()
                break
            elif opcao == 6:
                print("Volte sempre!")
                sleep(2)
                exit(0)
            else:
                print("Opção inválida! Por favor, escolha um número entre 1 e 6.")
                sleep(1)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")
            sleep(1)


def cadastrar_produto() -> None:
    print("Cadastro e Produto")
    print("==================")

    nome: str = input("Informe o nome do produto: ")
    preco: float = float(input("Informe o preço do produto: "))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f"O produto {produto.nome} foi cadastrado com sucesso!")
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print("Listagem de produtos")
        print("====================")
        for produto in produtos:
            print(produto)
            print("====================")
            sleep(1)
    else:
        print("Ainda não exitem produtos cadastrados.")
    sleep(2)
    menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print("Informe o código o produto que deseja adicionar ao carrinho: ")
        print("=============================================================")
        print("=================== Produtos Disponiveis ====================")
        for produto in produtos:
            print(produto)
            print("====================================================")
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(Produto)
                    if quant:
                        item[produto] = quant + 1
                        print(f"O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.")
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f"O produto {produto.nome} foi adicionado ao carrinho.")
                sleep(2)
                menu()
        else:
            print(f"O produto com código {codigo} não foi encontrado.")
            sleep(2)
            menu()
    else:
        print("Ainda não existem produtos para vender.")
    sleep(2)
    menu()

def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print("Produtos no carrinho: ")

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Qauntidade: {dados[1]}")
                print("=======================")
                sleep(1)
    else:
        print("Ainda não existem produtos no carrinho.")
    sleep(2)
    menu()

def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print("Produtos do Carrinho")
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f"Quantidade: {dados[1]}")
                valor_total += dados[0].preco * dados[1]
                print("============================")
                sleep(1)
        print(f"Sua fatura é {formata_float_str_moeda(valor_total)}")
        print("Volte sempre!")
        carrinho.clear()
        sleep(5)
    else:
        print("Ainda não existem produtos no carrinho")
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p

if __name__ == "__main__":
    main()