from Jogo.calcular import Calcular


def main() -> None:
        pontos: int = 0
        jogar(pontos)

def solicitar_dificuldade() -> int:
    while True:
        try:
            dificuldade = int(input("Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: "))
            if dificuldade in [1, 2, 3, 4]:
                return dificuldade
            else:
                print("Dificuldade inválida!")
        except ValueError:
            print("Dificuldade inválida!")

def solicitar_resposta() -> int:
    while True:
        try:
            resultado = int(input("Digite sua resposta: "))
            return resultado
        except ValueError:
            print("Resposta inválida! Por favor, insira um resultado inteiro.")

def continuar_jogo() -> int:
    while True:
        try:
            continuar = int(input("Deseja continuar no jogo? [1 - sim, 0 - não] "))
            if continuar in [0, 1]:
                return continuar
            else:
                print("Opção inválida!")
        except ValueError:
            print("Opção inválida!")

def jogar(pontos: int) -> None:
    dificuldade = solicitar_dificuldade()
    calc: Calcular = Calcular(dificuldade)

    print("Informe o resultado para a seguinte operação: ")
    calc.mostrar_operacao()

    resultado = solicitar_resposta()

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f"Você tem {pontos} ponto(s).")

    continuar = continuar_jogo()

    if continuar == 1:
        jogar(pontos)
    else:
        print(f"Você finalizou com {pontos} ponto(s).")
        print("Até a próxima!")

def main() -> None:
    pontos: int = 0
    jogar(pontos)

if __name__ == "__main__":
    main()
