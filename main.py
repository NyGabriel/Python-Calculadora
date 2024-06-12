# Definindo as funções para as operações matemáticas
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        return x / y

# Função principal para executar a calculadora
def main():
    while True:
        print("\nCalculadora")
        print("Escolha a operação:")
        print("1. Adicionar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")
        escolha = input("Digite sua opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo da calculadora...")
            break

        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print("Resultado: ", adicionar(num1, num2))
            elif escolha == '2':
                print("Resultado: ", subtrair(num1, num2))
            elif escolha == '3':
                print("Resultado: ", multiplicar(num1, num2))
            elif escolha == '4':
                resultado = dividir(num1, num2)
                print("Resultado: ", resultado)
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executando a função principal
if __name__ == "__main__":
    main()
