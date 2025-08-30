from statistic_calculator import StatisticCalculator

def main():
    print("=== Calculadora Estatística ===")
    entrada = input("Digite uma lista de números separados por espaço: ")
    numeros = [int(x) for x in entrada.split()]
    calc = StatisticCalculator(numeros)

    while True:
        print("\nEscolha uma operação:")
        print("1 - Média")
        print("2 - Mediana")
        print("3 - Maior valor")
        print("4 - Menor valor")
        print("5 - Desvio padrão")
        print("0 - Sair")
        opcao = input("> ")

        if opcao == "1":
            print("Média:", calc.media())
        elif opcao == "2":
            print("Mediana:", calc.mediana())
        elif opcao == "3":
            print("Maior:", calc.maior_valor())
        elif opcao == "4":
            print("Menor:", calc.menor_valor())
        elif opcao == "5":
            print("Desvio padrão:", calc.desvio_padrao())
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()