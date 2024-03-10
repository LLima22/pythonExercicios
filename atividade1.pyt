def maior_entre_n():
    numeros = []
    while True:
        numero = int(input("Digite um número (0 para parar): "))
        if numero == 0:
            break
        numeros.append(numero)
    if numeros:
        print("O maior número é:", max(numeros))
    else:
        print("Nenhum número foi inserido.")

maior_entre_n()
