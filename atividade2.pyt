def divisao():
    while True:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        if valor2 != 0:
            print("Resultado da divisão:", valor1 / valor2)
            break
        else:
            print("O segundo valor não pode ser zero. Tente novamente.")

divisao()
