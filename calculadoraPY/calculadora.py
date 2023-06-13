def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else: 
        return "Erro!"

def calculadora():
    print("Bem vindo a minha primeira calculadora!")
    print("selecione uma operação:")
    print("1 - adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")

    escolha = input("Digite o número da operação desejada: ")

    num1 = float(input("digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = 0

    if escolha == '1':
        resultado = adicao(num1, num2)
    elif escolha == '2':
        resultado = subtracao(num1, num2)
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
    elif escolha == '4':
        resultado = divisao(num1, num2)
    else:
        print("Opção inválida!")  

    print("O resultado é: ", resultado)

    calculadora()

