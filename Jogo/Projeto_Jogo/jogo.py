from Jogo.calcular import Calcular


def main() -> None:
        pontos: int = 0
        jogar(pontos)


def jogar(pontos: int) -> None:
    while True:
        try:
            dificuldade = int(input("Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: "))
            if dificuldade in [1, 2, 3, 4]:
                break
            else:
                print("Dificuldade inválida!")
        except ValueError:
            print("Dificuldade inválida!")

    calc: Calcular = Calcular(dificuldade)

    print("Informe o resultado para a seguinte operação: ")
    calc.mostrar_operacao()

    while True:
        try:
            resultado = int(input("Digite sua resposta: "))
            break
        except ValueError:
            print("Resposta inválida! Por favor, insira um resultado inteiro.")

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f"Você tem {pontos} ponto(s).")

    while True:
        try:
            continuar = int(input("Deseja continuar no jogo? [1 - sim, 0 - não] "))
            if continuar in [0, 1]:
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Opção inválida!")

    if continuar == 1:
        jogar(pontos)
    else:
        print(f"Você finalizou com {pontos} ponto(s).")
        print("Até a próxima!")


if __name__ == "__main__":
    main()
